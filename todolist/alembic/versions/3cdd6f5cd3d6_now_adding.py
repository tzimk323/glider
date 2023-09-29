"""NOW ADDING?

Revision ID: 3cdd6f5cd3d6
Revises: 7eac7b2b60ee
Create Date: 2023-09-25 22:28:34.632971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cdd6f5cd3d6'
down_revision: Union[str, None] = '7eac7b2b60ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
