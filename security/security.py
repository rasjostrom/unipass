
import pickle

from simplecrypt import encrypt, decrypt


def encrypt_and_pickle_dumps(data, key):
    cipher = encrypt(data, key)
    cipher_dump = pickle.dumps(cipher)
    return cipher_dump


def decrypt_and_pickle_loads(data, key):
    cipher_dump = pickle.loads(data)
    plaintext = decrypt(cipher_dump, key)
    return plaintext



