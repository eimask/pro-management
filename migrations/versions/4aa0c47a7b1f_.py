"""empty message

Revision ID: 4aa0c47a7b1f
Revises: fdc174dede78
Create Date: 2018-02-06 18:30:18.374013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aa0c47a7b1f'
down_revision = 'fdc174dede78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('USER', sa.Column('created_by', sa.Integer(), nullable=True))
    op.add_column('USER', sa.Column('is_supervisor', sa.Boolean(), nullable=True))
    op.add_column('USER', sa.Column('modified_by', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('USER', 'modified_by')
    op.drop_column('USER', 'is_supervisor')
    op.drop_column('USER', 'created_by')
    # ### end Alembic commands ###
