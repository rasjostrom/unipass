import unittest
import os

from unipass.model.models import Service
from unipass.model.models import initdb


class DBTest(unittest.TestCase):

    def setUp(self):
        initdb()

    def tearDown(self):
        try:
            os.remove("sqlite3.db")
        except OSError:
            pass

    def test_create_none(self):
        self.user = Service()
        self.user.admin = True
        self.user.name = 'John'
        self.user.password = 'password'
        self.user.create()
        self.assertTrue(self.user.valid())
        self.assertTrue(self.user in Service.getall())

    def test_update_none(self):
        self.user = Service()
        self.user.admin = True
        self.user.name = 'John'
        self.user.password = 'password'
        self.user.create()
        self.user = Service.getbyuuid(self.user._uuid)
        self.user.name = 'Kalle'
        self.user.update()
        self.assertTrue(self.user in Service.getall())

    def test_delete_none(self):
        self.user = Service()
        self.user.admin = True
        self.user.name = 'John'
        self.user.password = 'password'
        self.user.create()
        self.user.delete()
        self.assertFalse(self.user in Service.getall())


