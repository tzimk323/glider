"""new table added

Revision ID: 34e135f81f70
Revises: 49eadd1ed4ab
Create Date: 2023-09-25 22:18:55.470153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34e135f81f70'
down_revision: Union[str, None] = '49eadd1ed4ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
