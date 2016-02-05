import unittest

from model.models import User


class DescriptorTest(unittest.TestCase):

    def test_AdminDescriptor_True_True(self):
        self.user = User()
        self.user.admin = True
        self.assertTrue(self.user._admin)

    def test_AdminDescriptor_False_True(self):
        self.user = User()
        self.user.admin = False
        self.assertFalse(self.user._admin)

    def test_AdminDescriptor_string_False(self):
        self.user = User()
        with self.assertRaises(ValueError):
            self.user.admin = 'notAbool'
        self.assertFalse(self.user.admin)

