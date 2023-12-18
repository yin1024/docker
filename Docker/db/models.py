from .database import Base
from sqlalchemy import Column, JSON, Integer, String


class DbHomework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True, index=True)
    school = Column(String)
    semester = Column(String)
    workName = Column(String)
    githubUrl = Column(String)
    websiteUrl = Column(String)
    pptUrl = Column(String)
    imgUrl = Column(String)
    skill = Column(JSON)
    name = Column(JSON)
