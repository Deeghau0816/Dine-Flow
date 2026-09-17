from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    categoryName: str
    categoryImage: str | None = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    categoryName: str | None = None
    categoryImage: str | None = None


class CategoryResponse(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)