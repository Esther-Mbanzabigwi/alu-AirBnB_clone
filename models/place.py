<<<<<<< HEAD
#!/usr/bin/python3
"""
Module documentation
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Model """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
=======
#!/usr/bin/python3
""" Place class """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
>>>>>>> ac9420e7d7b307ba5d5ce47970877a097d4d2bae
