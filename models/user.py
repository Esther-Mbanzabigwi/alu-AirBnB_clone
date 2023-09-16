<<<<<<< HEAD
#!/usr/bin/python3
"""
Module documentation
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
=======
#!/usr/bin/python3
""" User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
>>>>>>> ac9420e7d7b307ba5d5ce47970877a097d4d2bae
