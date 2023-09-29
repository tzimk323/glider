"""test4

Revision ID: ac4d318443a8
Revises: 3cdd6f5cd3d6
Create Date: 2023-09-25 22:51:40.024599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac4d318443a8'
down_revision: Union[str, None] = '3cdd6f5cd3d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
