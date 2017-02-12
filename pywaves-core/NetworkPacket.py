import struct


class NetworkPacket(object):
    packet_struct_template = "!i{message_length}B"

    def __init__(self, message):
        self.message = message
        self.message_length = len(self.message)

        self.packet_struct = struct.Struct(self.packet_struct_template.format(message_length=self.message_length))

    def get_bytes(self):
        return self.packet_struct.pack(self.message_length, *self.message)
