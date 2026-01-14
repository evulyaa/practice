from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)

    # Связь с книгами
    books = relationship("Book", back_populates="category_rel")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    url = Column(String, nullable=True) # Пока пустая
    
    # Внешний ключ на категорию
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Связь с таблицей категорий
    category_rel = relationship("Category", back_populates="books")
