#!/usr/bin/python3
# The basemodel of the AIRBnB clone

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ base class for all classes"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """readable representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.created_at = datetime.now()
    
    def to_dict(self):
        my_dictionary = self.__dict__.copy()
        my_dictionary['__class__']= self.__class__.__name__
        my_dictionary['created_at'] = self.created_at.isoformat()
        my_dictionary['updated_at'] =  self.updated_at.isoformat()
        return my_dictionary

