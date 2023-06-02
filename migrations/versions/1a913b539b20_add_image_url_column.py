"""Add image_url column

Revision ID: 1a913b539b20
Revises: fcf1cf4d9e46
Create Date: 2023-06-02 10:40:09.600027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a913b539b20'
down_revision = 'fcf1cf4d9e46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###