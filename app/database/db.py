from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER=os.environ.get("DATABASE_USER")
DATABASE_PASSWORD=os.environ.get("DATABASE_PASSWORD") 
DATABASE_HOST=os.environ.get("DATABASE_HOST")

SQLALCHEMY_DATABASE_URL = "sqlite:///./phonebook.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:RsOUXuROlrbMlzx3aNiq@containers-us-west-101.railway.app:6064/railway"
# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
       db = SessionLocal()
       try:
           yield db
       finally:
           db.close()
