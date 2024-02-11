#!/usr/bin/python3
from models.base_model import BaseModel

#Module name : State


class State(BaseModel):
#what is class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor way """
        super().__init__(self, *args, **kwargs)
