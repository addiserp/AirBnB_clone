#!/usr/bin/python3

"""
It defines the User class.
a class User that inherits from BaseModel:
"""

from models.base_model import BaseModel
import json


class User(BaseModel):

    """
    A inherited from BaseModel class which represent a user.

    Public class attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
