from app.db.db import SessionLocal, engine, Base
from app.db import crud

def init():

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    
    try:
        print("Добавление категорий...")
        cat_sf = crud.create_category(db, title="Научная фантастика")
        cat_dev = crud.create_category(db, title="Программирование")

        print("Добавление книг...")
        crud.create_book(
            db, title="Дюна", description="Легендарный роман Фрэнка Герберта", 
            price=1200.50, category_id=cat_sf.id
        )
        crud.create_book(
            db, title="Основание", description="Цикл романов Айзека Азимова", 
            price=950.00, category_id=cat_sf.id
        )

        crud.create_book(
            db, title="Чистый код", description="Руководство по написанию хорошего кода", 
            price=2500.00, category_id=cat_dev.id
        )
        crud.create_book(
            db, title="Изучаем Python", description="Классический учебник Марка Лутца", 
            price=3200.00, category_id=cat_dev.id
        )
        crud.create_book(
            db, title="Грокаем алгоритмы", description="Иллюстрированное пособие для программистов", 
            price=1800.00, category_id=cat_dev.id
        )

        print("База данных успешно инициализирована и наполнена!")

    except Exception as e:
        print(f"Ошибка при наполнении БД: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init()
