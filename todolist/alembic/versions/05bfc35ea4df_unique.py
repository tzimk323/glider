"""unique

Revision ID: 05bfc35ea4df
Revises: ac4d318443a8
Create Date: 2023-09-25 23:01:15.830776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05bfc35ea4df'
down_revision: Union[str, None] = 'ac4d318443a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
