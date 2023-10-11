#!/usr/bin/python3

"""
A module for City class, it is a subclass of BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):

    """
    inherited from BaseModel class which represent a city.

    Public class attributes:
        state_id (str): The state id
        name (str): The city name
    """

    state_id = ""
    name = ""
