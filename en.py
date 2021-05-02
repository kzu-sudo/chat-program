#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto import Random


class cr(object):

    def __init__(self, key):
        self.key = key
        self.iv = b"abcdefghijklmnop"

    def d_en(self, message):
        o = AES.new(self.key, AES.MODE_CFB, self.iv)
        data = message
        data = o.encrypt(data)
        return data

    def d_de(self, message):
        o = AES.new(self.key, AES.MODE_CFB, self.iv)
        data = o.decrypt(message)
        return data
