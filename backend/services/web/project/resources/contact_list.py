from flask_restful import Resource, reqparse
from ..models.person_contact_info import PersonContactInfo, person_contact_info_schema, person_contact_infos_schema
from .. import db
from flask import jsonify, make_response

parser = reqparse.RequestParser()
parser.add_argument('info')
parser.add_argument('typeId')


class ContactList(Resource):
    def get(self, person_id):
        contact_infos = PersonContactInfo.query.filter_by(
            person_id=person_id).all()
        return make_response(jsonify(person_contact_infos_schema.dump(contact_infos)), 200)

    def post(self, person_id):
        args = parser.parse_args()
        contact_info = PersonContactInfo(info=args['info'],
                                         person_id=person_id, type_id=args['typeId'])
        db.session.add(contact_info)
        db.session.commit()
        return make_response(jsonify(person_contact_info_schema.dump(contact_info)), 201)
