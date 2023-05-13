from fastapi import FastAPI
from app.models import models
from app.database.db import engine

from app.routers import phonebook


app = FastAPI(title="Phonebook App",
              description="A platform where users can manage  \
              their contacts",
              version="1.0.0")


from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["set-cookie"],
)


@app.get('/')
def root():
    return {"Hello": "world"}

app.include_router(phonebook.phonebook_router)


