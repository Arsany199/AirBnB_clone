#!/usr/bin/python3
"""this difines the filestorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """this is the abstracted storage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key (obj class name).id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serialization of __object to JSON file"""
        obdict = FileStorage.__objects
        objdict = {obj: obdict[obj].to_dict() for obj in obdict.keys()}
        with open(FileStorage.__file_path) as fil:
            json.dump(objdict, fil)

    def reload(self):
        """deserialization the JSON file"""
        try:
            with open(FileStorage.__file_path) as fil:
                objdict = json.load(fil)
                for i in objdict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return
