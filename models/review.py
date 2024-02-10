#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
#file name: review


class Review(BaseModel):
    """definition for class Review"""
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
#def init in consuctor way
        super().__init__(self, *args, **kwargs)
