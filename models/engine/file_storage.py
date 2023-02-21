#!/usr/bin/python3
""" file storage """
import json


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
        with open(self.__file_path, mode="a", encoding="utf-8") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as json_file:
                new_dict = json.load(json_file)
                for key, value in new_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)
        except:
            pass
