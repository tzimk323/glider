"""unique7

Revision ID: 81f4945bbc6f
Revises: 66419212ac9c
Create Date: 2023-09-25 23:06:18.063199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81f4945bbc6f'
down_revision: Union[str, None] = '66419212ac9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
