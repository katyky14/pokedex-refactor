from enum import Enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PokemonTypes(Enum):
  fire = 1
  electric = 2
  normal = 3
  ghost = 4
  psychic = 5
  water = 6
  bug = 7
  dragon = 8
  grass = 9
  fighting = 10
  ice = 11
  flying = 12
  poison = 13
  ground = 14
  rock = 15
  steel = 16


class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    type = db.Column(db.Enum(PokemonTypes), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounteredRate = db.Column(db.Float)
    catchRate = db.Column(db.Float)
    captured = db.Column(db.Boolean)
