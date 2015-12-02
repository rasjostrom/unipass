
import unittest
import os

from model.models import User, Entry
from model.models import initdb


class UserTest(unittest.TestCase):

    def setUp(self):
        initdb()

    def tearDown(self):
        try:
            os.remove("sqlite3.db")
        except OSError:
            pass

    def test_user_create(self):
        self.user = User()
        self.user.name = "John"
        self.user.password = "password"
        self.assertTrue(self.user.create())

    def test_user_create_no_password(self):
        self.user = User()
        self.user.name = "John"
        self.user.password = ""
        self.assertTrue(self.user.create())

    def test_user_create_no_username_and_no_password(self):
        self.user = User()
        self.user.name = ""
        self.user.password = ""
        self.assertTrue(self.user.create())

    def test_get_user_by_name(self):
        self.assertTrue("John" in [user.name for user in User.getall()])







