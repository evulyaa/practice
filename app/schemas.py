from pydantic import BaseModel, ConfigDict
from typing import List, Optional

# Схемы для Книг
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    url: Optional[str] = None
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# Схемы для Категорий
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    books: List[BookResponse] = []
    model_config = ConfigDict(from_attributes=True)
