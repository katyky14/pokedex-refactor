from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class PokemonForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=255, message="must be between 3 and 255 characters")]])
    attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(min=0, max=100, message=None)])
    defense = IntegerField("Defense", validators=[DataRequired(), NumberRange(min=0, max=100, message=None)])
    imageurl = StringField("ImageUrl", validators=[DataRequired()])
    move1 = StringField("move1", validators=[DataRequired()])
    move2 = StringField("move2")
    number = IntegerField("Number", validators=[DataRequired()])
    type = SelectField("Type", choices=[])
    submit = SubmitField("Create New Pokemon")
    cancel = SubmitField("Cancel")

class EditPokemonForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=255, message="must be between 3 and 255 characters")])
    attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(min=0, max=100, message=None)])
    defense = IntegerField("Defense", validators=[DataRequired(), NumberRange(min=0, max=100, message=None)])
    imageurl = StringField("ImageUrl", validators=[DataRequired()])
    move1 = StringField("move1", validators=[DataRequired()])
    move2 = StringField("move2")
    number = IntegerField("Number", validators=[DataRequired()])
    type = SelectField("Type", choices=[])
    submit = SubmitField("Edit Pokemon")
    cancel = SubmitField("Cancel")

class ItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=1, max=255, message=None)])
    happiness = IntegerField("Happiness", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    submit = SubmitField("Add Item")
    cancel = SubmitField("Cancel")

class EditItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=1, max=255, message=None)])
    happiness = IntegerField("Happiness", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    submit = SubmitField("Edit Item")
    cancel = SubmitField("Cancel")
