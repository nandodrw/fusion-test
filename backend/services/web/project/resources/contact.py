from flask_restful import Resource, reqparse
from ..models.person_contact_info import PersonContactInfo, person_contact_info_schema
from .. import db
from flask import jsonify, make_response

parser = reqparse.RequestParser()
parser.add_argument('info')
parser.add_argument('typeId')


class Contact(Resource):
    def get(self, person_id, contact_id):
        contact_info = PersonContactInfo.query.get(contact_id)
        return make_response(jsonify(person_contact_info_schema.dump(contact_info)), 200)

    def delete(self, person_id, contact_id):
        contact_info = PersonContactInfo.query.get(contact_id)
        db.session.delete(contact_info)
        db.session.commit()
        return '', 204

    def put(self, person_id, contact_id):
        args = parser.parse_args()
        contact_info = PersonContactInfo.query.get(contact_id)
        contact_info.info = args['info']
        contact_info.type_id = args['typeId']
        db.session.commit()
        return '', 204
