import datetime
import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Teacher(SqlAlchemyBase):
    __tablename__ = 'teachers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    available_dates = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    subjects = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # student = orm.relation("Teacher", back_populates='teacher')
