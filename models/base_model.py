#!/usr/bin/python3
# The basemodel of the AIRBnB clone

from uuid import uuid4
from datetime import datetime


# class BaseModel:
#     """ base class for all classes"""
#     def __init__(self):
#         self.id = str(uuid4())
#         self.created_at = datetime.now()
#         self.updated_at = datetime.now()

#     def __str__(self):
#         """readable representation"""
#         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

#     def save(self):
#         """updates created_at when instance changes"""
#         self.created_at = datetime.now()
    
#     def to_dict(self):
#         """ print a dictionary with instances as keys"""
#         my_dictionary = self.__dict__.copy()
#         my_dictionary['__class__'] = self.__class__.__name__
#         my_dictionary['created_at'] = self.created_at.isoformat()
#         my_dictionary['updated_at'] =  self.updated_at.isoformat()
#         return my_dictionary


class BaseModel:
    '''Updated new base class for all classes'''


    def __init__(self, *args, **kwargs):
        """new instance"""
        if kwargs.__len__() > 0:
            for k, v in kwargs.items():
               if k == 'created_at' or k == 'updated_at':
                   value = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                   setattr(self, k, value)
                   continue
               if k != '__class__':
                   setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at= datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """readable representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the value of updated_at when instance changes"""
        self.updated_at= datetime.now()
    
    def to_dict(self):
        """ print a dictionary with instances as keys"""
        my_dictionary = self.__dict__.copy()
        my_dictionary['__class__'] = self.__class__.__name__
        my_dictionary['created_at'] = self.created_at.isoformat()
        my_dictionary['updated_at'] =  self.updated_at.isoformat()
        return my_dictionary
