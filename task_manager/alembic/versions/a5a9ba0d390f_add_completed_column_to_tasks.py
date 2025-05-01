"""Add completed column to tasks

Revision ID: a5a9ba0d390f
Revises: 
Create Date: 2025-04-30 20:02:33.379301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a5a9ba0d390f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
