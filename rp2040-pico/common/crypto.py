import uos
from ucryptolib import aes

BLOCK_SIZE = 16

class CryptoAesECB:
    def __init__(self, key: str=None, mode: int=None):
        self.key = key or 'd37ac63b612149219bc6c82d48902151'
        self.mode = mode or 1

    def encrypt(self, plaintext: str) -> bytes:
        """AES ECB"""
        self.aes = aes(self.key, self.mode)
        plaintext = plaintext + " "*(BLOCK_SIZE - len(plaintext) % BLOCK_SIZE)
        encrypted = self.aes.encrypt(plaintext)
        return encrypted

    def decrypt(self, encrypted: bytes) -> bytes:
        """AES ECB"""
        self.aes = aes(self.key, self.mode)
        plaintext = self.aes.decrypt(encrypted)
        return plaintext


class CryptoAesCBC:
    def __init__(self, key: str=None, mode: int=None):
        self.key = key or 'd37ac63b612149219bc6c82d48902151'
        self.mode = mode or 2
        self.iv = uos.urandom(BLOCK_SIZE)

    def encrypt(self, plaintext: str) -> bytes:
        self.aes = aes(self.key, self.mode, self.iv)
        plaintext = plaintext + " "*(BLOCK_SIZE - len(plaintext) % BLOCK_SIZE)
        encrypted = self.aes.encrypt(plaintext)
        return encrypted

    def decrypt(self, encrypted: bytes) -> bytes:
        self.aes = aes(self.key, self.mode, self.iv)
        decrypted = self.aes.decrypt(encrypted)
        return decrypted


if __name__ == '__main__':
    cae = CryptoAesECB()
    e = cae.encrypt('123456')
    p = cae.decrypt(e)
    print(e, p)

    cac = CryptoAesCBC()
    e = cac.encrypt('123456')
    p = cac.decrypt(e)
    print(e, p)
