import struct

import WavesCrypto
from NetworkPacket import NetworkPacket


class NetworkMessage(NetworkPacket):
    magic = b"\x12\x34\x56\x78"
    message_struct_template = "<4BBi4B{payload_length}B"

    def __init__(self, message_type, payload):
        self.message_type = message_type

        self.payload = payload
        payload_length = len(self.payload)
        payload_checksum = WavesCrypto.fast_hash(self.payload)[0:4]

        message_struct = struct.Struct(self.message_struct_template.format(payload_length=payload_length))

        message = message_struct.pack(*self.magic, self.message_type, payload_length, payload_checksum,
                                      *self.payload)

        super().__init__(message)
