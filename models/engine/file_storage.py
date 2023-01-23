#!/usr/bin/python3
""" serialization and deserialization"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    class that serializes instances to a JSON file 
    and deserializes JSON file to  instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in  __objects the obj with key(<obj class name>.id)
        """
        self. __objects["{obj.__class__.name__}.{obj.id}"]= obj

    def save(self):
        """
        serializes __objects to JSON file
        """
        with open(FileStorage.__file_path, mode= 'w') as file:
            empty_dict = {}
            for k, val in self.__objects.items():
                empty_dict[k] = val.to_dict()
            json.dump(empty_dict, file)

    def reload(self):
        """deserializes json file to __objects
        if the Json file exists"""
        new_dict = {}
        try:
            with open(FileStorage.__file_path, mode= 'r') as file:
                new_dict = json.load(file)
                for k, val in new_dict.items():
                    self.__objects[k] = eval(val['__class__'])(**val)

        except FileNotFoundError:
            pass

