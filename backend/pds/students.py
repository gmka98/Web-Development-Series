from sqlalchemy import Integer, Column, String
from pds.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    status = Column(String, nullable=False)