#!/usr/bin/python3
""" unique instance for my application """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
