import binascii
import unittest

from Handshake import HandshakeBuilder, Handshake


class HandshakeTests(unittest.TestCase):
    def test_creation(self):
        h = Handshake("test-app", "1.2.3", "test-node", 1234567890, "127.0.0.1:12345", 1234567890)
        self.assertEqual(
            b"0000003b08746573742d61707000000001000000020000000309746573742d6e6f646500000000499602d2000000087f0000010000303900000000499602d2",
            binascii.hexlify(h.get_bytes()))

    def test_1(self):
        hb = HandshakeBuilder("test-name", "1.2.3", "test-node", "192.168.0.1:65500")
        h = hb.build()
        bs = binascii.hexlify(h.get_bytes())

        self.assertEqual(b"0000003c09746573742d6e616d6500000001000000020000000309746573742d6e6f6465", bs[0:-56])


if __name__ == '__main__':
    unittest.main()
