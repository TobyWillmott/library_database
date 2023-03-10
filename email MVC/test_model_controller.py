import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from controller import Controller
from model import Base, Email


class TestModel:
    @pytest.fixture()
    def setup_db(self):
        engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(engine)
        with Session(engine) as sess:
            yield sess

    def test_email(self, setup_db):
        email = Email(email_address='andrew@dales.com', password="Hello@99")
        assert email.email_address == 'andrew@dales.com'

    def test_database(self, setup_db):
        sess = setup_db
        test1 = Email(email_address="tobwil0910@highgateschool.org.uk", password="P@ssword100")
        test2 = Email(email_address="toby@willmott.com", password="Ch@rlie33")
        sess.add(test1)
        sess.add(test2)
        sess.commit()
        assert sess.query(Email).count() == 2
        first_test = sess.query(Email).first()
        assert first_test.email_address == "tobwil0910@highgateschool.org.uk"


class Controller:
    def __init__(self, db_name='emails.sqlite'):
        self.engine = create_engine(f'sqlite:///{db_name}', echo=True)


class TestController:
    @pytest.fixture()
    def setup_controller(self):
        controller = Controller(':memory:')
        Base.metadata.create_all(controller.engine)
        return controller

    def test_save(self, setup_controller):
        controller = setup_controller
        temp_email = 'bill@ms.com'
        temp_password = "P@assword101"
        save_message = controller.save(temp_email, temp_password)
        assert save_message == f"The email {temp_email} saved!"

    def test_save_wrong_email(self, setup_controller):
        controller = setup_controller
        with pytest.raises(ValueError) as error:
            controller.save('not_correct')
            assert str(error.value) == 'Invalid email address'
