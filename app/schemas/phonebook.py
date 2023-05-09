from pydantic import BaseModel, Field
from typing import Optional


class Phonebook(BaseModel):
    firstname: str
    lastname: str 
    phone_number:str = Field(max_length=10)