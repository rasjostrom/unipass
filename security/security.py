from blowfish import Cipher as cipher


class Crypto(object):

    @staticmethod
    def encrypt(self, data, key):
        return str(b"".join(cipher.encrypt_cbc(data, key)))

    @staticmethod
    def decrypt(self, data, key):
        return str(b"".join(cipher.decrypt_cbc(data, key)))


