"""new table added 22222222222

Revision ID: 7eac7b2b60ee
Revises: 34e135f81f70
Create Date: 2023-09-25 22:22:08.509785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7eac7b2b60ee'
down_revision: Union[str, None] = '34e135f81f70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
