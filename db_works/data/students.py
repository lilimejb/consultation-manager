import datetime
import sqlalchemy

from .db_session import SqlAlchemyBase


class Student(SqlAlchemyBase):
    __tablename__ = 'students'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    wanted_date = sqlalchemy.Column(sqlalchemy.DateTime)
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("teachers.id"))
