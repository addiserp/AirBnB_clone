#!/usr/bin/python3

"""__init__ magic FileStorage for models directory"""


from models.engine.file_storage import FileStorage

STORAGE = FileStorage()
STORAGE.reload()
