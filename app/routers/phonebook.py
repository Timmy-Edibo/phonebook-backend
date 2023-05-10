from fastapi import APIRouter, Depends
from pydantic import EmailStr


from app.database.db import get_db
from sqlalchemy.orm import Session

# from app.cruds import users
from app.cruds import phonebook
from app.schemas.phonebook import Phonebook


phonebook_router = APIRouter(prefix="/api/v1/phonebook", tags=['phonebook'])


@phonebook_router.get("/get/{id}")
def get_phonebook(id: int, db:Session=Depends(get_db)):
    
   return phonebook.get_phonebook(id, db)
    
@phonebook_router.get("/list-all")
def list_phonebook(db:Session=  Depends(get_db)):
    return phonebook.list_phonebook_users(db)

@phonebook_router.post("/create")
async def  create_phonebook(request: Phonebook, db: Session = Depends(get_db)):
    return phonebook.register_user(request, db)


@phonebook_router.put("/update/{id}")
def update_phonebook(id:int, request: Phonebook, db:Session=Depends(get_db)):
    
    return phonebook.update_user(id, request, db)


@phonebook_router.delete("/delete/{id}")
def delete_phonebook(id: int, db:Session=Depends(get_db)):
    
    return phonebook.delete_user(id, db)


@phonebook_router.post("/search")
def search_phonebook_user(lastname: str, db:Session=Depends(get_db)):
    
    return phonebook.search_phonebook_user(lastname, db)

