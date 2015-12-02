
from blowfish import Cipher as cipher


class Crypto(object):

    def __init__(self, iv):
        self.iv = iv

    def encrypt(self, data):
        return b"".join(cipher.encrypt_cbc(data, self.iv))

    def decrypt(self, data):
        return b"".join(cipher.decrypt_cbc(data, self.iv))


