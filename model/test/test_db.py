import unittest
import os

from model.models import User
from model.models import initdb


class DBTest(unittest.TestCase):

    def setUp(self):
        initdb()

    def tearDown(self):
        try:
            os.remove("sqlite3.db")
        except OSError:
            pass

    def test_create_none(self):
        self.user = User()
        self.user.admin = True
        self.user.name = 'John'
        self.user.password = 'password'
        self.user.create()
        self.assertTrue(self.user.valid())
        self.assertTrue(self.user._admin)

    def test_AdminDescriptor_False_True(self):
        self.user = User()
        self.admin = False
        self.assertFalse(self.admin)
