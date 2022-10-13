from flask import Blueprint, redirect
from ..forms import PokemonForm,EditItemForm,EditPokemonForm,ItemForm
from ..models import db,Pokemon,PokemonTypes,Item

bp = Blueprint("pokemon",__name__,url_prefix="/api")

@bp.route("/pokemon")
def pokemon():
    pokemon=(Pokemon.query.all())
    print("POKEMON",pokemon)
    
    return pokemon



@bp.route("/",methods=["POST"])
def createpokemon():
    addForm = PokemonForm()
    if addForm.validate_on_submit():
        data = Pokemon()
        addForm.populate_obj(data)
        db.session.add(data)
        db.session.commit()
        print("DATA FROM POST",data)
        return redirect('/pokemon')

@bp.route("/<int:id>",methods=["PUT"])
def editpokemon(id):
    editForm = EditPokemonForm()
    if editForm.validate_on_submit():
        data = Pokemon()
        editForm.populate_obj(data)
        db.session.add(data)
        db.session.commit()
    return Pokemon.query.get(id)





