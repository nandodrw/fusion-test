from flask_restful import Resource, reqparse
from ..models.person import Person as PersonModel, person_schema
from ..models.person_contact_info import PersonContactInfo
from .. import db
from flask import jsonify, make_response

parser = reqparse.RequestParser()
parser.add_argument('firstName')
parser.add_argument('lastName')
parser.add_argument('birthDate')


class Person(Resource):
    def get(self, person_id):
        person = PersonModel.query.get(person_id)
        return make_response(jsonify(person_schema.dump(person)), 200)

    def delete(self, person_id):
        person = PersonModel.query.get(person_id)
        contact_info = PersonContactInfo.query.filter_by(person=person).all()
        for info in contact_info:
            db.session.delete(info)
        db.session.delete(person)
        db.session.commit()
        return '', 204

    def put(self, person_id):
        args = parser.parse_args()
        person = PersonModel.query.get(person_id)
        person.first_name = args['firstName']
        person.last_name = args['lastName']
        person.date_of_birth = args['birthDate']
        db.session.commit()
        return '', 204
