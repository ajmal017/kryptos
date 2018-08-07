"""empty message

Revision ID: 5e29ad8a0e89
Revises: 6c6917015a3c
Create Date: 2018-07-24 19:55:21.518610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e29ad8a0e89'
down_revision = '6c6917015a3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('telegram_auth_date', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('telegram_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('telegram_photo', sa.String(), nullable=True))
    op.add_column('users', sa.Column('telegram_username', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'users', ['telegram_username'])
    op.create_unique_constraint(None, 'users', ['telegram_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'telegram_username')
    op.drop_column('users', 'telegram_photo')
    op.drop_column('users', 'telegram_id')
    op.drop_column('users', 'telegram_auth_date')
    # ### end Alembic commands ###