from sqlalchemy import Integer, Column, String, Boolean
from sqlalchemy.orm import Session

from pds.database import Base
from pds.security import get_password_hash


class User(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    deleted = Column(Boolean, nullable=False, default=False)


class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, email: str, password: str):
        user = User(email=email, password=get_password_hash(password))
        self.session.add(user)
        self.session.commit()
        return user
