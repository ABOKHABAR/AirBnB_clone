#!/usr/bin/python3
from models.base_model import BaseModel
"""
file City name
"""


class City(BaseModel):
    """definition for class City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ def init """
        super().__init__(self, *args, **kwargs)
