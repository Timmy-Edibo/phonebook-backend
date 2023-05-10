from pydantic import BaseModel, Field, validator
from typing import Optional


class Phonebook(BaseModel):
    firstname: str = Field(min_length=3)
    lastname: str = Field(min_length=3)
    phone_number:str = Field(max_length=10, min_length=10)
    
    # @validator('lastname')
    # def validate_lastname(cls, values):
    #     ph = values.get('lastname')
    
    #     if not isinstance(ph, str):
    #         raise ValueError('Value must be a string')
    
  