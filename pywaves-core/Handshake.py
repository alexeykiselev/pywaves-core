import random
import struct
import time

from NetworkAddress import NetworkAddress
from NetworkPacket import NetworkPacket
from Version import Version


class Handshake(NetworkPacket):
    handshake_struct_template = ">B{application_name_length}BIIIB{node_name_length}BqI{address_length}BQ"

    def __init__(self, application_name, version, node_name, nonce, node_address, timestamp):
        v = Version(version)
        address = NetworkAddress.from_string(node_address)
        address_bytes = address.get_bytes()
        address_bytes_len = len(address_bytes)

        application_name_bytes = bytes(application_name, "utf-8")
        application_name_bytes_len = len(application_name_bytes)

        node_name_bytes = bytes(node_name, "utf-8")
        node_name_bytes_len = len(node_name_bytes)

        handshake_struct = struct.Struct(self.handshake_struct_template.format(
            application_name_length=application_name_bytes_len,
            node_name_length=node_name_bytes_len,
            address_length=address_bytes_len))

        handshake = handshake_struct.pack(application_name_bytes_len, *application_name_bytes, v.major, v.minor,
                                          v.patch, node_name_bytes_len, *node_name_bytes, nonce, address_bytes_len,
                                          *address_bytes, timestamp)

        super().__init__(handshake)


class HandshakeBuilder(object):
    def __init__(self, application_name, version, node_name, address):
        self.application_name = application_name
        self.version = version
        self.node_name = node_name
        self.nonce = random.choice(range(-2147483648, 2147483647))
        self.address = address

    def build(self):
        timestamp = int(time.time())

        return Handshake(self.application_name, self.version, self.node_name, self.nonce, self.address, timestamp)
