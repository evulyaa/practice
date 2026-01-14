from app.db.db import SessionLocal
from app.db import crud

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
