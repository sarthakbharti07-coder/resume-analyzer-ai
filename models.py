from sqlalchemy import Column, Integer, String, Text, ForeignKey
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(200), unique=True)
    password = Column(String(100))


class reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    resume_text = Column(Text)
    result = Column(Text)
