# -*- coding: utf-8 -*-

import unittest

from unipass.security.security import AESCipher as aes
from unipass.model.models import Service


class SecurityTest(unittest.TestCase):

    def test_AESCipher_ServiceObject_True(self):
        self.user = Service(_name='John', _password='password', _service='gmail')
        self.cipher = aes('my_key').encrypt(self.user.__dict__)
        me = Service(**(aes('my_key').decrypt(self.cipher)))
        self.assertEquals('John', me.name)
        self.assertEquals('password', me.password)
        self.assertEquals('gmail', me.service)
        


