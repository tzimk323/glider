"""unique2

Revision ID: 66419212ac9c
Revises: 05bfc35ea4df
Create Date: 2023-09-25 23:04:00.765538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66419212ac9c'
down_revision: Union[str, None] = '05bfc35ea4df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
