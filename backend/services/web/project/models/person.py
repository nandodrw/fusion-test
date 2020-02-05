from .. import db
from .. import ma
from ..models.contact_info_type import *


class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), unique=False)
    last_name = db.Column(db.String(128), unique=False)
    date_of_birth = db.Column(db.String(128), unique=False)

    def __init__(self, first_name, last_name, date_of_birth=""):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
