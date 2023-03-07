from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import Email


class Controller:
    def __init__(self):
        self.engine = create_engine("sqlite:///email.sqlite", echo=True)

    def save(self, email, secret):
        """
        Save the email
        :param secret:
        :param email:
        :return:
        """
        try:

            with Session(self.engine) as sess:
                email_address = Email(email_address=email, password=secret)
                sess.add(email_address)
                sess.commit()

                return "saved"


        except ValueError as error:
            # show an error message
            raise ValueError(error)
