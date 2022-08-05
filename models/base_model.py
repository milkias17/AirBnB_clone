#!/usr/bin/python3
"""define all common attribute/method for other classes"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """parent class of AirBnB project"""

    def __init__(self):
        """initialize id, created_at, updated_at"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """updates the updated_at public instance attribute"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns dictionary of key/value of __dict__
        key __class__ added to the dictionary
        """
        dicti = self.__dict__.copy()
        dicti['created_at'] = self.created_at.isoformat()
        dicti['updated_at'] = self.updated_at.isoformat()
        dicti['__class__'] = self.__class__.__name__

        return dicti

    def __str__(self):
        """print in a format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        