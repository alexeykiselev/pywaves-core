import struct

import base58

import WavesCrypto


class WavesAddress(object):
    """
    Blockchain address basic representation.

    Attributes:
        public_key: A public key ofr address
    """
    version = 1
    scheme = 'S'
    data_struct = struct.Struct("<BB20B")
    address_struct = struct.Struct("<BB20B4B")

    def __init__(self, public_key):
        self.public_key = public_key
        self.public_key_hash = WavesCrypto.secure_hash(self.public_key)[0:20]

    def address(self):
        schema_byte = ord(self.scheme)
        data = self.data_struct.pack(self.version, schema_byte, *self.public_key_hash)
        pk_checksum = self.checksum(data)

        return self.address_struct.pack(self.version, schema_byte, *self.public_key_hash, *pk_checksum)

    def address_string(self):
        return base58.b58encode(self.address())

    @staticmethod
    def checksum(message):
        return WavesCrypto.secure_hash(message)[0:4]


class TestNetAddress(WavesAddress):
    """
    Address for TestNet
    """
    scheme = 'T'


class MainNetAddress(WavesAddress):
    """
    Address for MainNet
    """
    scheme = 'W'
