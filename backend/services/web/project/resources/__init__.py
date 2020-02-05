from flask_restful import Api
from project.resources.people_list import PeopleList
from project.resources.person import Person
from project.resources.contact_list import ContactList
from project.resources.contact import Contact
from project.resources.contact_type_list import ContactTypeList


def generate_api(app):
    api = Api(app)
    api.add_resource(PeopleList, '/api/people')
    api.add_resource(Person, '/api/people/<person_id>')
    api.add_resource(ContactList, '/api/people/<person_id>/contact')
    api.add_resource(Contact, '/api/people/<person_id>/contact/<contact_id>')
    api.add_resource(ContactTypeList, '/api/contact-type')
