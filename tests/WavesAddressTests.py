import binascii
import unittest

import base58

from WavesAddress import MainNetAddress, TestNetAddress


class WavesAddressTests(unittest.TestCase):
    def test_base58_decode(self):
        encoded = "5jpwaJnERa8Gr1ChgrNYnmxm2EtZ4KHC5bW1ZLL7LCY1bUV9gFWFAGjpJaPDCawmFzguqGBgYDyeocpEsKWeYDM1"
        decoded = base58.b58decode(encoded)

        self.assertEqual(b"ecffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f" +
                         b"0000000000000000000000000000000000000000000000000000000000000000", binascii.hexlify(decoded))

    def test_main_net_address_1(self):
        public_key = binascii.unhexlify(b"0100000000000000000000000000000000000000000000000000000000000000")
        address = MainNetAddress(public_key).address_string()
        self.assertEqual("3P89Gonteikxhpup4ExAf5SaQyHVzeQqvNg", address)

    def test_test_net_address_1(self):
        public_key = binascii.unhexlify(b"ecffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff7f")
        address = TestNetAddress(public_key).address_string()
        self.assertEqual("3N5VeQvxGy9LJNXZoSNKU7NNqFptBUdnyLL", address)


if __name__ == '__main__':
    unittest.main()
