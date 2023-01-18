#!/usr/bin/python3
# The basemodel of the AIRBnB clone

from uuid import uuid4
import datetime


class BaseModel:
    """ base class for all classes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """readable representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        