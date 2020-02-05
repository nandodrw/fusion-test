from .. import db
from .. import ma
from ..models.contact_info_type import *


class PersonContactInfo(db.Model):
    __tablename__ = "person_contact_info"

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(128), unique=False)

    person_id = db.Column(db.Integer, db.ForeignKey(
        'people.id'), nullable=False)
    person = db.relationship(
        'Person', backref=db.backref('person', lazy=False))

    type_id = db.Column(db.Integer, db.ForeignKey(
        'contact_info_types.id'), nullable=False)
    type = db.relationship(
        'ContactInfoType', backref=db.backref('infos', lazy=True))

    __table_args__ = (
        db.UniqueConstraint('person_id', 'type_id',
                            'info', name='_unique_contact_data'),
    )


class PersonContactInfoSchema(ma.ModelSchema):
    class Meta:
        model = PersonContactInfo


person_contact_info_schema = PersonContactInfoSchema()
person_contact_infos_schema = PersonContactInfoSchema(many=True)
