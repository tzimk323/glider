"""anotha

Revision ID: 97e6fd8366cd
Revises: 3e6643c4559a
Create Date: 2023-09-26 11:57:48.067601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97e6fd8366cd'
down_revision: Union[str, None] = '3e6643c4559a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
