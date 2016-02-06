import unittest
import os

from controller import controller
from model.models import initdb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ControllerTest(unittest.TestCase):

    def setUp(self):
        initdb()

    def tearDown(self):
        try:
            print(os.path.join(BASE_DIR, 'db.sqlite3'))
            #os.remove(os.path.join(BASE_DIR, 'db.sqlite3'))
        except OSError:
            pass

    def test_createAdmin_True(self):
        self.assertTrue(controller.create_user('john', 'password'))

    def test_addService_True(self):
        self.assertTrue(controller.add_service('facebook', 'jherrin@gmail.com', 'password', 'facebook acc'))



