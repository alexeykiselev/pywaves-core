import ipaddress

import struct


class NetworkAddress(object):
    network_address_struct = struct.Struct(">LI")

    def __init__(self, address, port):
        self.ip_address = ipaddress.ip_address(address)
        self.port = port

    @classmethod
    def from_string(cls, address_string):
        parts = address_string.split(":")

        return cls(parts[0], int(parts[1]))

    def get_bytes(self):
        return self.network_address_struct.pack(int(self.ip_address), self.port)
