"""for adding new column

Revision ID: 6fe583395531
Revises: e62b37f7198b
Create Date: 2025-11-16 23:06:30.519617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fe583395531'
down_revision: Union[str, Sequence[str], None] = 'e62b37f7198b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts",'content')
    pass
