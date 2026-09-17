from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.categories import Category
from app.schemas.categories import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)

import app.services.category_services as category_service


router = APIRouter(
    prefix="/api/categories",
    tags=["Categories"],
)


# CREATE
@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    existing_category = (
        db.query(Category)
        .filter(Category.categoryName == category.categoryName)
        .first()
    )

    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exists",
        )

    return category_service.create_category(
        db,
        category,
    )


# READ ALL
@router.get(
    "/",
    response_model=list[CategoryResponse],
)
def get_categories(
    db: Session = Depends(get_db),
):
    return category_service.get_categories(db)


# READ ONE
@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    category = category_service.get_category(
        db,
        category_id,
    )

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


# UPDATE
@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
):
    updated_category = category_service.update_category(
        db,
        category_id,
        category,
    )

    if not updated_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return updated_category


# DELETE
@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    deleted_category = category_service.delete_category(
        db,
        category_id,
    )

    if not deleted_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return None