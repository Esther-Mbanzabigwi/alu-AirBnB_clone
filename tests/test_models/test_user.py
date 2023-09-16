#!/usr/bin/python3
""" unit test for class User """

from models import User
import unittest


class TestUser(unittest.TestCase):
    """Test Cases for User model
    """

    def test_email(self):
        """Test user mail"""
        user = User()
        self.assertEqual(user.email, "")
        user.email = "gnondoyixavier@gmail.com"
        self.assertEqual(user.email, "gnondoyixavier@gmail.com")

    def test_password(self):
        """Test user password"""
        user = User()
        self.assertEqual(user.password, "")
        user.password = "Gnondohi00?"
        self.assertEqual(user.password, "Gnondohi00?")

    def test_first_name(self):
        """Test user first_name"""
        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "xavier"
        self.assertEqual(user.first_name, "xavier")

    def test_last_name(self):
        """Test user last_name"""
        user = User()
        self.assertEqual(user.last_name, "")
        user.last_name = "Gnondoyi"
        self.assertEqual(user.last_name, "Gnondoyi")


if __name__ == "__main__":
    unittest.main()
