from .. import db
from .. import ma


class ContactInfoType(db.Model):
    __tablename__ = "contact_info_types"

    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(128), unique=True)


class ContactInfoTypeSchema(ma.ModelSchema):
    class Meta:
        model = ContactInfoType


person_contact_info_types_schema = ContactInfoTypeSchema(many=True)
