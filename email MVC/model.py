from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, validates
import re

Base = declarative_base()
class Email(Base):
    __tablename__= "email"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String, nullable=False)
    password = Column(String, nullable=False)
    def __repr__(self):
        return f"Email:{self.email_address}"


    @validates("email_address")
    def validate_email(self, key, address):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(pattern, address):
            raise ValueError("Invalid email address")
        if key != "email_address":
            raise ValueError("Key must be 'email'")
        return address

    @validates("password")
    def validate_password(self, key, password):
        pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if not re.fullmatch(pattern, password):
            raise ValueError("Invalid password")
        if key != "password":
            raise ValueError("Key must be 'password'")
        return password