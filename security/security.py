
class Crypto(object):

    def __init__(self, iv):
        self.iv = iv

    def encrypt(data):
        return data_encrypted = b"".join(cipher.encrypt_cbc(data, self.iv))


    def decrypt(data):
        return data_decrypted = b"".join(cipher.decrypt_cbc(data, self.iv))
        
