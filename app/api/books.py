from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..db import crud, db, models
from .. import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[schemas.BookResponse])
def list_books(
    category_id: Optional[int] = Query(None, description="Фильтр по ID категории"),
    session: Session = Depends(db.get_db)
):
    query = session.query(models.Book)
    if category_id:
        query = query.filter(models.Book.category_id == category_id)
    return query.all()

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, session: Session = Depends(db.get_db)):
    category = session.query(models.Category).filter(models.Category.id == book.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Указанная категория не существует")
    
    return crud.create_book(
        db=session, title=book.title, description=book.description, 
        price=book.price, category_id=book.category_id, url=book.url
    )

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, session: Session = Depends(db.get_db)):
    book = crud.get_book_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_data: schemas.BookUpdate, session: Session = Depends(db.get_db)):
    if book_data.category_id:
        category = session.query(models.Category).filter(models.Category.id == book_data.category_id).first()
        if not category:
            raise HTTPException(status_code=400, detail="Указанная категория не существует")
            
    updated_book = crud.update_book(session, book_id, book_data.model_dump(exclude_unset=True))
    if not updated_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return updated_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, session: Session = Depends(db.get_db)):
    if not crud.delete_book(session, book_id):
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return None
