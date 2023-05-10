from fastapi import ( Depends, HTTPException, status)
from sqlalchemy import func


from app.schemas.phonebook import Phonebook
from app.models import models
from app.database.db import get_db
from sqlalchemy.orm import Session


def  register_user(request: Phonebook, db: Session = Depends(get_db)):
    
    user_request = models.Phonebook(**request.dict())
    db.add(user_request)
    db.commit()
    db.refresh(user_request)
         
    return user_request

def get_phonebook(id: int, db:Session=Depends(get_db)):
    
    if query :=  db.query(models.Phonebook).filter(
        models.Phonebook.id == id).first():
        return {"data": query, "status": status.HTTP_201_CREATED}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="User not found in Phonebook")

def list_phonebook_users(db:Session=  Depends(get_db)):
    query =  db.query(models.Phonebook).all()
    response = query if len(query) > 0 else "No record found in db"
    return {"data": response, "status": status.HTTP_200_OK}


def update_user(id:int, request: Phonebook, db:Session=Depends(get_db)):
    query =  db.query(models.Phonebook).filter(models.Phonebook.id == id)
    
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="User not found in phonebook")
            
    query.update(request.dict(),synchronize_session=False)
    db.commit()      
    return {"data": query.first(), "status": status.HTTP_200_OK}
        

def delete_user(id: int, db:Session=Depends(get_db)):
    
    if query :=  db.query(models.Phonebook).filter(
        models.Phonebook.id == id).first():
        db.delete(query)
        db.commit()
        
        return {"data": "User deleted from phonebook successfully", "status": status.HTTP_200_OK}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="User not found in phonebook")
    
def search_phonebook_user(lastname: str, db:Session=Depends(get_db)):
    query =  db.query(models.Phonebook).filter(
        func.lower(models.Phonebook.lastname).like(func.lower(f"%{lastname}%"))
    ).all()
    
    # db.query(models.Phonebook).filter(
    #     models.Phonebook.lastname == lastname).first()
    
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="User not found in phonebook")
        
    return {"data": query, "status": status.HTTP_200_OK}


# def delete_all_user(db:Session=  Depends(get_db)):
#     query =  db.query(models.User).all()
    
#     for user in query:
#         user = db.query(models.User).filter(models.User.id == user.id).first()
#         otp = db.query(models.Otp).filter(models.Otp.email == user.email).first()
#         db.delete(otp)
#         db.delete(user)
#         db.commit()
    
#     return {"data": "Users deleted successfully", "status": status.HTTP_200_OK}

