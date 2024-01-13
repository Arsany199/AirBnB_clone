#!/usr/bin/python3
"""this modeule defines the review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """this is the review class"""
    place_id = ""
    user_id = ""
    text = ""
