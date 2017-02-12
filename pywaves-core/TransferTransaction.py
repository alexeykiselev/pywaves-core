import math
import time

class TransferTransaction(object):
    transaction_type = 4

    def __init__(self, sender_pk, recipient_address, amount, fee, timestamp, attachment, signature):
        self.sender_pk = sender_pk
        self.recipient_address = recipient_address
        self.amount = amount
        self.fee = fee
        self.timestamp = timestamp
        self.attachment = attachment
        self.signature = signature

    def bytes(self):

        return result


class TransferTransactionFactory(object):
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    def bytes_to_sign(self, amount, fee, recipient_address):
        timestamp = math.floor(time.time()).as_integer_ratio()
        timestamp_bytes = WavesUtils.long_to_bytes(timestamp, endianness="little", width=8)
        amount_bytes = WavesUtils.long_to_bytes(amount, endianness="little", width=8)
        fee_bytes = WavesUtils.long_to_bytes(fee, endianness="little", width=8)

        result = TransferTransaction.transaction_type + self.public_key + b"\00\00" + timestamp_bytes + amount_bytes + fee_bytes + recipient_address + b"\00\00"

        return result

    def createTransaction(self, recipient_address, amount, fee):
