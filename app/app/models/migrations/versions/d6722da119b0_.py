"""empty message

Revision ID: d6722da119b0
Revises: 9d05939446cd
Create Date: 2018-07-27 20:32:29.741736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6722da119b0'
down_revision = '9d05939446cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('strategies', sa.Column('results_json', sa.JSON(), nullable=True))
    op.add_column('strategies', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('strategies', 'status')
    op.drop_column('strategies', 'results_json')
    # ### end Alembic commands ###
