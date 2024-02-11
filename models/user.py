#!/usr/bin/python

#class user

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''model base 12'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
