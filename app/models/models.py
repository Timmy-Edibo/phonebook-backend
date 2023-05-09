from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.database.db import Base
from datetime import datetime, timedelta, timezone


class Phonebook(Base):
    __tablename__ = "phonebook"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(20))
    lastname = Column(String(20))
    phone_number =Column(String(20))