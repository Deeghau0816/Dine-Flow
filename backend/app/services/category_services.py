from sqlalchemy.orm import Session

from app.models.categories import Category
from app.schemas.categories import (
    CategoryCreate,
    CategoryUpdate,
)


def create_category(
    db: Session,
    category: CategoryCreate,
):
    db_category = Category(
        categoryName=category.categoryName,
        categoryImage=category.categoryImage,
    )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def get_categories(
    db: Session,
):
    return db.query(Category).all()


def get_category(
    db: Session,
    category_id: int,
):
    return (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )


def update_category(
    db: Session,
    category_id: int,
    category: CategoryUpdate,
):
    db_category = (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

    if not db_category:
        return None

    if category.categoryName is not None:
        db_category.categoryName = category.categoryName

    if category.categoryImage is not None:
        db_category.categoryImage = category.categoryImage

    db.commit()
    db.refresh(db_category)

    return db_category


def delete_category(
    db: Session,
    category_id: int,
):
    db_category = (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

    if not db_category:
        return None

    db.delete(db_category)
    db.commit()

    return db_category1