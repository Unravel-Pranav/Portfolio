from pydantic import BaseModel, EmailStr

class ContactBase(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactCreate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True
