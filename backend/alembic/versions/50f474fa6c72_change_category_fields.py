"""change category fields

Revision ID: 50f474fa6c72
Revises: f19869f7ee60
Create Date: 2026-09-17 13:32:08.387865
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "50f474fa6c72"
down_revision: Union[str, Sequence[str], None] = "f19869f7ee60"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # Rename existing name column
    op.alter_column(
        "categories",
        "name",
        new_column_name="categoryName"
    )

    # Remove old unique constraint
    op.drop_constraint(
        "categories_name_key",
        "categories",
        type_="unique"
    )

    # Create unique constraint for renamed column
    op.create_unique_constraint(
        "uq_categories_categoryName",
        "categories",
        ["categoryName"]
    )

    # Add category image
    op.add_column(
        "categories",
        sa.Column(
            "categoryImage",
            sa.String(length=500),
            nullable=True
        )
    )

    # Remove old slug constraint and column
    op.drop_constraint(
        "categories_slug_key",
        "categories",
        type_="unique"
    )

    op.drop_column(
        "categories",
        "slug"
    )


def downgrade() -> None:

    # Re-create slug
    op.add_column(
        "categories",
        sa.Column(
            "slug",
            sa.String(length=100),
            nullable=True
        )
    )

    # Remove category image
    op.drop_column(
        "categories",
        "categoryImage"
    )

    # Remove categoryName unique constraint
    op.drop_constraint(
        "uq_categories_categoryName",
        "categories",
        type_="unique"
    )

    # Rename categoryName back to name
    op.alter_column(
        "categories",
        "categoryName",
        new_column_name="name"
    )

    # Restore name unique constraint
    op.create_unique_constraint(
        "categories_name_key",
        "categories",
        ["name"]
    )