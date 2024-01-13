#!/usr/bin/python3
"""this for the definition of the basemodel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """this reprisent the basemodel class"""

    def __init__(self, *args, **kwargs):
        """init of my attributes"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetimedatetime.strptime(val, tform)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """renew the updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
