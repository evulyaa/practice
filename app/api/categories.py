from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..db import crud, db
from .. import schemas

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[schemas.CategoryResponse])
def list_categories(session: Session = Depends(db.get_db)):
    return crud.get_categories(session)

@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def get_category(category_id: int, session: Session = Depends(db.get_db)):
    category = session.query(db.models.Category).filter(db.models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category

@router.post("/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, session: Session = Depends(db.get_db)):
    return crud.create_category(session, title=category.title)

@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, category_data: schemas.CategoryUpdate, session: Session = Depends(db.get_db)):
    updated_cat = crud.update_category(session, category_id, category_data.title)
    if not updated_cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return updated_cat

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, session: Session = Depends(db.get_db)):
    if not crud.delete_category(session, category_id):
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return None
