import curve25519
import pyblake2

import sha3


def secure_hash(message):
    blake_hash = pyblake2.blake2b(digest_size=32)
    blake_hash.update(message)
    m1 = blake_hash.digest()

    keccak_hash = sha3.keccak_256()
    keccak_hash.update(m1)
    m2 = keccak_hash.digest()

    return m2


def fast_hash(message):
    blake_hash = pyblake2.blake2b(digest_size=32)
    blake_hash.update(message)

    return blake_hash.digest()


def sign(private_key, message):
    return curve25519.shared(private_key, message)
