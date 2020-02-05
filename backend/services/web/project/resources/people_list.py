from flask_restful import Resource, reqparse
from ..models.person import Person, people_schema, person_schema
from .. import db
from flask import jsonify, make_response


parser = reqparse.RequestParser()
parser.add_argument('firstName')
parser.add_argument('lastName')
parser.add_argument('birthDate')


class PeopleList(Resource):
    def get(self):
        people = Person.query.all()
        return make_response(jsonify(people_schema.dump(people)), 200)

    def post(self):
        args = parser.parse_args()
        print(args['firstName'])
        new_person = Person(first_name=args['firstName'],
                            last_name=args['lastName'], date_of_birth=args['birthDate'])
        db.session.add(new_person)
        db.session.commit()
        return make_response(jsonify(person_schema.dump(new_person)), 201)
