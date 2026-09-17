from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    categoryName: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    categoryImage: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )