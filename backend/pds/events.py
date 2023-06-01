from sqlalchemy import Integer, Column, String

from pds.database import Base


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)