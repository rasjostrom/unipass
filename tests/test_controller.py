import unittest
import os

from unipass.controller import controller
from unipass.model.models import initdb

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ControllerTest(unittest.TestCase):

    def setUp(self):
        initdb()

    def tearDown(self):
        try:
            os.remove('sqlite3.db')
            os.remove('unipass_export.json')
        except OSError:
            pass

    def test_createAdmin_True(self):
        self.assertTrue(controller.create_user('john', 'password'))

    def test_addService_True(self):
        self.assertTrue(controller.add_service('facebook', 'jherrin@gmail.com', 'password', 'facebook acc'))

    def test_login_True(self):
        self.assertTrue(controller.create_user('admin', 'password'))
        self.assertTrue(controller.login('admin', 'password'))

    def test_exportData_True(self):
        self.assertTrue(controller.create_user('john', 'password'))
        self.assertTrue(controller.export_data())

    def test_exportData_False(self):
        self.assertTrue(controller.export_data())

    def test_importData_False(self):
        self.assertFalse(controller.import_data(path=BASE_DIR+'/broken.json'))

    def test_importData_True(self):
        self.assertTrue(controller.import_data(path=BASE_DIR+'/correct.json'))




