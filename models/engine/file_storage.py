#!/usr/bin/python3
""" file storage """
import json
from models.base_model import BaseModel


class FileStorage:
    """ file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_file:
                new_dict = json.load(json_file)
                cls = "__class__"
                for key, value in new_dict.items():
                    class_name = key.split('.')
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
