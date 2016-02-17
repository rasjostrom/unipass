
import base64
from Crypto import Random
from Crypto.Cipher import AES
import md5
import ast

# http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
# http://code.runnable.com/UwdZzhi2XsttAAAU/crypto-example-for-python

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AESCipher(object):
    
    def __init__( self, key ):
        self.key = md5.new(key).digest()

    def encrypt( self, raw ):
        raw = pad(str(raw))
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return ast.literal_eval(unpad(cipher.decrypt( enc[16:] )))

