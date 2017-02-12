import unittest

import binascii

from NetworkAddress import NetworkAddress


class NetworkAddressTests(unittest.TestCase):
    def test_creation(self):
        a = NetworkAddress("127.0.0.1", 12345)
        self.assertEqual(b"7f00000100003039", binascii.hexlify(a.get_bytes()))

    def test_creation_from_string(self):
        a = NetworkAddress.from_string("127.0.0.1:12345")
        self.assertEqual(b"7f00000100003039", binascii.hexlify(a.get_bytes()))

    def test_creation_from_string_2(self):
        a = NetworkAddress.from_string("192.168.0.1:65500")
        self.assertEqual(b"c0a800010000ffdc", binascii.hexlify(a.get_bytes()))




if __name__ == '__main__':
    unittest.main()
