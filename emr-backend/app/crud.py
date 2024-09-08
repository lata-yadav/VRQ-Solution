from sqlalchemy.orm import Session
from app import models, schemas

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(name=patient.name, email=patient.email,prescription=None)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def update_patient_prescription(db: Session, patient_id: int, prescription_path: str):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient:
        patient.prescription = prescription_path
        db.commit()
        db.refresh(patient)
    return patient
