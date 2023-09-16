<<<<<<< HEAD
#!/usr/bin/python3
"""
This module defines a base class for
all models in our hbnb clone
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel that defines all common
    attributes/methods for other classe
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """Representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
=======
#!/usr/bin/python3
""" Module for Base """

from datetime import datetime
from uuid import uuid4
import json
import models

format_date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Basemodel class """

    def __init__(self, *args, **kwargs):
        """ Initialization of Database """
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_date)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str definition"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save definition"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
>>>>>>> ac9420e7d7b307ba5d5ce47970877a097d4d2bae
