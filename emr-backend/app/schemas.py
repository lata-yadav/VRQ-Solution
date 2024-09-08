from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    email: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    prescription: str

    class Config:
        orm_mode = True
