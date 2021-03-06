#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """a public object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """define the method parameter"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save the json string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([
                    obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """return the list of the json string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                return [cls.create(**d)
                        for d in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save the json string representation to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([
                    obj.to_dictionary() for obj in list_objs]))

    @classmethod
    def load_from_file_csv(cls):
        """return a list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                return [cls.create(**d)
                        for d in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
