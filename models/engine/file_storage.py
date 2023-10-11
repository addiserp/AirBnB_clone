#!/usr/bin/python3
'''
It is a Class for file_storage serializes and deserializes JSON types
'''


import json
from models.base_model import BaseModel


class FileStorage:

    """
    This is a storage engine for AirBnB project

    Class Methods:
        new: updates the dictionary.id
        all: Returns the object self
        reload: Deserializes and converts JSON strings into Python objects.
        save: Serializes and converts Python objects into JSON strings.


    Class Attributes:
        __objects (dict): A dictionary of instantiated objects.
        __file_path (str): The name of the file to save objects to.
    """

    __file_path = 'airbnbfile.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel}
    def all(self):

        '''
        Return dictionary of <class>.<id> : object instance
        '''
        return self.__objects

    def new(self, obj):

        '''
        new __objects to existing dictionary of instances
        '''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):

        """
        Save/serialize obj dictionaries to json file
        """
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):

        """
        Deserialize/convert obj dicts back to instances, if it exists
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
