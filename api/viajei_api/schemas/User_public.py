from pydantic import BaseModel, EmailStr 
class UserPublic(BaseModel):
    email:EmailStr