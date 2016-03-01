
import unittest

from unipass.model.models import Service


class DescriptorTest(unittest.TestCase):

    def test_AdminDescriptor_True_True(self):
        self.user = Service()
        self.user.admin = True
        self.assertTrue(self.user.admin)

    def test_AdminDescriptor_False_True(self):
        self.user = Service()
        self.user.admin = False
        self.assertFalse(self.user.admin)

    def test_AdminDescriptor_string_False(self):
        self.user = Service()
        with self.assertRaises(ValueError):
            self.user.admin = 'notAbool'
        self.assertFalse(self.user.admin)

