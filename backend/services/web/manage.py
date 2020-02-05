from flask.cli import FlaskGroup

from project import app, db
from project.resources import generate_api
from project.models.contact_info_type import ContactInfoType
from project.models.person import Person
from project.models.person_contact_info import PersonContactInfo


cli = FlaskGroup(app)
generate_api(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    address_type = ContactInfoType(desc="address")
    phone_type = ContactInfoType(desc="phone")
    email_type = ContactInfoType(desc="email")

    root_user = Person(first_name="Fernando",
                       last_name="Catacora", date_of_birth="10-10-2034")

    contactMethod1 = PersonContactInfo(
        info="nando.drw@gmail.com", person=root_user, type=email_type)
    contactMethod2 = PersonContactInfo(
        info="f.catacora@pucp.edu.pe", person=root_user, type=email_type)
    contactMethod3 = PersonContactInfo(
        info="+51 910 947 226", person=root_user, type=phone_type)

    test_user = Person(first_name="Jhon",
                       last_name="Bonachon", date_of_birth="10-10-2034")

    contactMethod4 = PersonContactInfo(
        info="jhon.bonachon@gmail.com", person=test_user, type=email_type)
    contactMethod5 = PersonContactInfo(
        info="123 Far Avenue", person=test_user, type=address_type)
    contactMethod6 = PersonContactInfo(
        info="+1 910 325 715", person=test_user, type=phone_type)

    db.session.add(contactMethod1)
    db.session.add(contactMethod2)
    db.session.add(contactMethod3)
    db.session.add(contactMethod4)
    db.session.add(contactMethod5)
    db.session.add(contactMethod6)
    db.session.commit()


if __name__ == "__main__":
    cli()
