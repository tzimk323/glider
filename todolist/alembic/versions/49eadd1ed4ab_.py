"""empty message

Revision ID: 49eadd1ed4ab
Revises: dcd979e1c588
Create Date: 2023-09-25 22:12:52.542248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49eadd1ed4ab'
down_revision: Union[str, None] = 'dcd979e1c588'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
