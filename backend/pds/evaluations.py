from sqlalchemy import Integer, Column, String

from pds.database import Base


class Evaluation(Base):
    __tablename__ = "evaluations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
    active_participation = Column(String, nullable=False)
    behavior = Column(String, nullable=False)
    acquisition_of_knowledge = Column(String, nullable=False)
    comments = Column(String, nullable=True)
