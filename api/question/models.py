from sqlalchemy import (Column, String, Integer, Boolean)
from sqlalchemy.orm import relationship, validates

from helpers.database import Base
from utilities.utility import Utility
import api.response.models


class Question(Base, Utility):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_type = Column(String, nullable=False)
    question = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    total_views = Column(Integer, default=0)
    response = relationship('Response', cascade="all, delete-orphan")
    is_active = Column(Boolean, default=False)

    @validates('question_type')
    def convert_capitalize(self, key, value):
        return value.lower()

    @property
    def question_response_count(self):
        ResponseModel = api.response.models.Response
        return ResponseModel.query.filter_by(question_id=self.id).count()
