"""Add role to Administrator

Revision ID: 3809910b4e56
Revises: 
Create Date: 2024-05-13 11:25:49.408134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3809910b4e56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('administrator', schema=None) as batch_op:
        # batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=False))
        pass  # Ensures that Python recognizes this block as syntactically correct

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('administrator', schema=None) as batch_op:
        # batch_op.drop_column('role')
        pass  # Include pass here as well, if no actions are taken in the downgrade block

    # ### end Alembic commands ###