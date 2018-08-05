"""empty message

Revision ID: 5aff868dc9db
Revises: 4aa0c47a7b1f
Create Date: 2018-02-18 02:14:11.734935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5aff868dc9db'
down_revision = '4aa0c47a7b1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'ROLE', ['role_code'])
    op.add_column('USER_ROLE', sa.Column('role_code', sa.String(length=50), nullable=False))
    op.add_column('USER_ROLE', sa.Column('username', sa.String(length=128), nullable=False))
    op.drop_column('USER_ROLE', 'user_id')
    op.drop_column('USER_ROLE', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('USER_ROLE', sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('USER_ROLE', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('USER_ROLE', 'username')
    op.drop_column('USER_ROLE', 'role_code')
    op.drop_constraint(None, 'ROLE', type_='unique')
    # ### end Alembic commands ###