from pydantic import BaseModel, Field, validator
from typing import Optional


class Phonebook(BaseModel):
    firstname: str = Field(min_length=3, title="First Name", example="John")
    lastname: str = Field(min_length=3, title="Last Name", example="Doe")
    phone_number: str = Field(max_length=10, min_length=10, title="Phone Number", example="1234567890")
    
    
    # @validator('lastname')
    # def validate_lastname(cls, values):
    #     ph = values.get('lastname')
    
    #     if not isinstance(ph, str):
    #         raise ValueError('Value must be a string')
    
  