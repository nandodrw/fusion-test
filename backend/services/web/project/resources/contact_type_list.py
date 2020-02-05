from flask_restful import Resource, reqparse
from ..models.person import ContactInfoType, person_contact_info_types_schema
from .. import db
from flask import jsonify, make_response


class ContactTypeList(Resource):
    def get(self):
        contact_types = ContactInfoType.query.all()
        return make_response(jsonify(person_contact_info_types_schema.dump(contact_types)), 200)
