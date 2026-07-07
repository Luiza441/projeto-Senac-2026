from pydantic import BaseModel


class Story:

    name:str
    title:str
    email = User.email
    body:str

