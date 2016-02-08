# -*- coding: utf-8 -*-

import unittest

from unipass.security.security import encrypt_and_pickle_dumps, decrypt_and_pickle_loads


# class CryptoTest(unittest.TestCase):
#
#     def test_Crypto_Str_True(self):
#         self.password = 'password'
#         self.key = 'a'
#         self.cipher_pickled = encrypt_and_pickle_dumps(self.password, self.key)
#         self.assertEquals(self.password, decrypt_and_pickle_loads(self.cipher_pickled, self.key))

    # def test_Crypto_StrSwe_True(self):
    #     self.password = 'passwordåäöÅÄÖ'
    #     self.key = 'a'
    #     self.cipher_pickled = encrypt_and_pickle_dumps(self.password, self.key)
    #     self.assertEquals(self.password, decrypt_and_pickle_loads(self.cipher_pickled, self.key))
    #
    # def test_Crypto_StrPol_True(self):
    #     self.password = 'passwordidziewążwąskądróżką'
    #     self.key = 'a'
    #     self.cipher_pickled = encrypt_and_pickle_dumps(self.password, self.key)
    #     self.assertEquals(self.password, decrypt_and_pickle_loads(self.cipher_pickled, self.key))


