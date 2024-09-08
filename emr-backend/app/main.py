from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app import models, schemas, crud, database
from app.email_utils import send_email
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os



app = FastAPI()

origins = ["http://localhost:3000"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new patient
@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db=db, patient=patient)

# Get all patients
@app.get("/patients/", response_model=List[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients

# Upload prescription
@app.post("/patients/{patient_id}/prescription/")
async def upload_prescription(patient_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    file_location = f"app/static/prescriptions/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Update patient record with prescription path
    crud.update_patient_prescription(db, patient_id, file_location)
    return {"filename": file.filename}

# Send follow-up email
@app.post("/patients/{patient_id}/followup/")
def send_followup(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    followup_message = f"Dear {patient.name},\nPlease schedule a follow-up appointment in 2 weeks."
    send_email(to_email=patient.email, subject="Follow-up Appointment", body=followup_message)
    
    return {"message": "Follow-up email sent"}
