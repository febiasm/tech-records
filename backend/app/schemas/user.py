from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str  # admin, engineer, qa, records

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool

model_config = {"from_attributes": True}
