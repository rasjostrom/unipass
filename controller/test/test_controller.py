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
            os.remove(os.path.join(BASE_DIR, 'db.sqlite3'))
        except OSError:
            pass

    def test_createAdmin_True(self):
        self.assertTrue(controller.create_admin('john', 'password'))
