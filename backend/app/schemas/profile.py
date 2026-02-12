from pydantic import BaseModel

class ProfileInfoResponse(BaseModel):
    name: str
    location: str
    year: int
