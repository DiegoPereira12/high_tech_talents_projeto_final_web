"""empty message

Revision ID: aa9ec6605ef5
Revises: 7d602c30beab
Create Date: 2022-05-23 19:51:30.877474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa9ec6605ef5'
down_revision = '7d602c30beab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluguel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_inquilino', sa.Integer(), nullable=False),
    sa.Column('id_imovel', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_imovel'], ['imovel.id'], ),
    sa.ForeignKeyConstraint(['id_inquilino'], ['inquilino.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aluguel')
    # ### end Alembic commands ###