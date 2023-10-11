#!/usr/bin/python3
"""
It defines Base for all the classes in the entire AirBnb project.
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """
    Base for all the classes in the entire AirBnb project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__(self): prints the class name, id, and creates dictionary
        representations of the input values
        __save(self): updates instance with current datetime atributes
        to_dict(self): returns the dictionary values of the instance obj
        __init__(self, *args, **kwargs)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize : uuid4, dates when class instance created.
        """
        dateF = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        dateF)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        dateF)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.STORAGE.new(self)

    def __str__(self):
        """
        Return class name, id, and the dictionary
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Instance method to:
        - update current datetime
        - invoke save() function &
        - save to serialized file
        """
        self.updated_at = datetime.now()
        models.STORAGE.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
