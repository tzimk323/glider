"""anotha

Revision ID: 814e1d39b31c
Revises: 97e6fd8366cd
Create Date: 2023-09-26 11:58:08.277002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '814e1d39b31c'
down_revision: Union[str, None] = '97e6fd8366cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
