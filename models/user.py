#!/usr/bin/python3
"""this module defines the user"""
from models.base_model import BaseModel


class User(BaseModel):
    """this is the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
