from app.db.db import SessionLocal
from app.db import crud

from fastapi import FastAPI
from .api import books, categories
from .db.db import engine, Base

def main():
    db = SessionLocal()
    
    try:
        print("ДАННЫЕ ИЗ БАЗЫ ДАННЫХ\n")

        print("Категории")
        categories = crud.get_categories(db)
        for cat in categories:
            print(f"[{cat.id}] {cat.title}")

        print("\nКниги")
        books = crud.get_books(db)
        for book in books:
            print(f"ID: {book.id} | Название: {book.title} | Цена: {book.price} руб. | Категория: {book.category_id}")

    finally:
        db.close()

if __name__ == "__main__":
    main()

#Задание 6
# Инициализация таблиц БД
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bookstore API",
    description="API для управления магазином книг",
    version="1.0.0"
)

# Подключение роутеров
app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health", tags=["System"])
def health_check():
    "Проверка работоспособности сервиса"
    return {"status": "ok", "message": "Service is alive"}

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "Добро пожаловать в Bookstore API! Перейдите в /docs, чтобы ознакомиться с интерфейсом Swagger."}