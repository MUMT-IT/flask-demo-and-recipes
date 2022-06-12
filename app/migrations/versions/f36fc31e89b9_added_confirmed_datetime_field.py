"""added confirmed datetime field

Revision ID: f36fc31e89b9
Revises: 5e046d909d78
Create Date: 2022-06-12 20:45:02.841000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f36fc31e89b9'
down_revision = '5e046d909d78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('confirmed_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appointments', 'confirmed_at')
    # ### end Alembic commands ###