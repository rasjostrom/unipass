import unittest
import os

from unipass.controller import controller
from unipass.model.models import initdb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ControllerTest(unittest.TestCase):

    def setUp(self):
        initdb()

    def tearDown(self):
        try:
            os.remove('sqlite3.db')
        except OSError:
            pass

    def test_createAdmin_True(self):
        self.assertTrue(controller.create_user('john', 'password'))

    def test_addService_True(self):
        self.assertTrue(controller.add_service('facebook', 'jherrin@gmail.com', 'password', 'facebook acc'))

    def test_login_True(self):
        self.assertTrue(controller.create_user('admin', 'password'))
        self.assertTrue(controller.login('admin', 'password'))





