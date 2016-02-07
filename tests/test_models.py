
import unittest
import os

from model.models import User
from model.models import initdb


class UserTest(unittest.TestCase):

    def setUp(self):
        initdb()

    def tearDown(self):
        try:
            os.remove("sqlite3.db")
        except OSError:
            pass

    def test_valid__returnFalse(self):
        self.user = User()
        self.assertFalse(self.user.valid())

    def test_valid_user_returnFalse(self):
        self.user = User()
        self.user.name = "John"
        self.assertFalse(self.user.valid())

    def test_valid_userPass_returnTrue(self):
        self.user = User()
        self.user.name = 'John'
        self.user.password = 'password'
        self.assertTrue(self.user.valid())

    def test_valid_userPassKWARGS_returnTrue(self):
        self.user = User(_name='John', _password='password')
        self.assertTrue(self.user.valid())




