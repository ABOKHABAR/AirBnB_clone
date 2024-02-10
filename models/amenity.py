#!/usr/bin/python3
from models.base_model import BaseModel
"""
Amenity
file
not empty
"""


class Amenity(BaseModel):
    """define this class Amenity 44"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ empty comment """
        super().__init__(self, *args, **kwargs)
