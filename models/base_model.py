#!/usr/bin/python3
""" base class """
import uuid
from datetime import datetime


class BaseModel:
    """ base class """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        return self.updated_at

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = __class__.__name__
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return new_dict
