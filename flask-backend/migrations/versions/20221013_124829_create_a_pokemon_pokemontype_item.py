"""Create a pokemon,pokemonType,item

Revision ID: f014d09b1f5c
Revises: 
Create Date: 2022-10-13 12:48:29.023130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f014d09b1f5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('imageUrl', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('fire', 'electric', 'normal', 'ghost', 'psychic', 'water', 'bug', 'dragon', 'grass', 'fighting', 'ice', 'flying', 'poison', 'ground', 'rock', 'steel', name='pokemontypes'), nullable=False),
    sa.Column('moves', sa.String(length=255), nullable=False),
    sa.Column('encounteredRate', sa.Float(), nullable=True),
    sa.Column('catchRate', sa.Float(), nullable=True),
    sa.Column('captured', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('number')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('happiness', sa.Integer(), nullable=True),
    sa.Column('imageUrl', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('pokemonId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemonId'], ['pokemons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('pokemons')
    # ### end Alembic commands ###