#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}
    # name = "FileStorage"

    # add cls parameter for taks 5
    # return a dictionary by class parameter
    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        # if a class is passed return dictionary with objects
        # of that class
        class_dict = {}
        # print("All FileStorage")
        for key, value in self.__objects.items():
            _class = value.__class__
            _value = value.__class__.__name__
            # _class = cls.__name__
            # _obj = type(value).__name__
            if cls == _class or cls == _value:
                # if _class == _obj:
                class_dict[key] = value
        return class_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' Delete an object from __objects if it’s inside '''
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    # added for AirBnB clone - Web framework
    # task 7
    def close(self):
        ''' call reload method'''
        self.reload()
