import binascii
import pyblake2
import unittest

import base58
import sha3

import WavesCrypto


class WavesCryptoTests(unittest.TestCase):
    def test_keccak_1(self):
        data = binascii.unhexlify(b"0100000000000000000000000000000000000000000000000000000000000000")
        kh = sha3.keccak_256()
        kh.update(data)
        h = kh.digest()
        self.assertEqual(b"48078cfed56339ea54962e72c37c7f588fc4f8e5bc173827ba75cb10a63a96a5", binascii.hexlify(h))

    def test_keccak_2(self):
        data = binascii.unhexlify(b"0000000000")
        kh = sha3.keccak_256()
        kh.update(data)
        h = kh.digest()
        self.assertEqual(b"c41589e7559804ea4a2080dad19d876a024ccb05117835447d72ce08c1d020ec", binascii.hexlify(h))

    def test_keccak_3(self):
        data = binascii.unhexlify(b"64617461")
        s = sha3.keccak_256()
        s.update(data)
        h = s.digest()
        self.assertEqual(b"8f54f1c2d0eb5771cd5bf67a6689fcd6eed9444d91a39e5ef32a9b4ae5ca14ff", binascii.hexlify(h))

    def test_blake_1(self):
        data = binascii.unhexlify(b"0100000000000000000000000000000000000000000000000000000000000000")
        s = pyblake2.blake2b(digest_size=32)
        s.update(data)
        h = s.digest()
        self.assertEqual(b"afbc1c053c2f278e3cbd4409c1c094f184aa459dd2f7fca96d6077730ab9ffe3", binascii.hexlify(h))

    def test_blake_2(self):
        data = binascii.unhexlify(b"0000000000")
        s = pyblake2.blake2b(digest_size=32)
        s.update(data)
        h = s.digest()
        self.assertEqual(b"569ed9e4a5463896190447e6ffe37c394c4d77ce470aa29ad762e0286b896832", binascii.hexlify(h))

    def test_blake_3(self):
        data = binascii.unhexlify(b"64617461")
        s = pyblake2.blake2b(digest_size=32)
        s.update(data)
        h = s.digest()
        self.assertEqual(b"a035872d6af8639ede962dfe7536b0c150b590f3234a922fb7064cd11971b58e", binascii.hexlify(h))

    def test_secure_hash_1(self):
        data = binascii.unhexlify(b"0100000000000000000000000000000000000000000000000000000000000000")
        h = WavesCrypto.secure_hash(data)
        self.assertEqual(b"44282d24d307fb66f385e9a814d07b693d17653c5b88d2e9d4e2a3ccc8216e10", binascii.hexlify(h))

    def test_secure_hash_2(self):
        data = binascii.unhexlify(b"0000000000")
        h = WavesCrypto.secure_hash(data)
        self.assertEqual(b"c67437bdaf6ed0ce5d3c39eb6dd591d8005fd0c1fb96cb134a6291ab8e1a39ac", binascii.hexlify(h))

    def test_secure_hash_3(self):
        data = binascii.unhexlify(b"64617461")
        h = WavesCrypto.secure_hash(data)
        self.assertEqual(b"7a21055775d130cdeb24258834f40cef7d9b0666f9b0f773cdd28ee556551bb0", binascii.hexlify(h))

    def test_signature(self):
        message = base58.b58decode("SdgxHQQb")
        private_key = base58.b58decode("5tyUbyyxWNaFU7aC4dA6FUPA5jqDxgVeqYrbzikCrpCw")
        expected_signature = \
            base58.b58decode("4V4aPf7WjpksMwMpGGSL6y8cLEt81FUGSdfVoTq3vHAv8xxxC8yrNYnAZNxfJvZBMVM1sBWFd4CnWQsWzZEKZfBh")

        actual_signature = WavesCrypto.sign(private_key, message)

        self.assertEqual(expected_signature, actual_signature)


if __name__ == '__main__':
    unittest.main()
