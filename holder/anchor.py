import base64
import os
import base58
import nacl.signing

def nacl_seed_to_did(seed):
    seed = seed_as_bytes(seed)
    vk = bytes(nacl.signing.SigningKey(seed).verify_key)
    did = base58.b58encode(vk[:16]).decode("ascii")
    verkey = base58.b58encode(vk).decode("ascii")
    return did, verkey

def seed_as_bytes(seed):
    if not seed or isinstance(seed, bytes):
        return seed
    if len(seed) != 32:
        return base64.b64decode(seed)
    return seed.encode("ascii")


class AnchorHandle:
    def __init__(self):
        self._did: str = None
        self._verkey: str = None

    @property
    def did(self):
        return self._did

    def seed_to_did(self, seed):
        return nacl_seed_to_did(seed)

    def generate_key(self, key_lenght=48):
        stream = os.popen(f'openssl rand -base64 {key_lenght}')
        output = stream.read()
        return output[:-1]
    
    def generate_seed(self):
        key = self.generate_key(32)
        stream = os.popen(f'echo "{key}" | fold -w 32 | head -n 1')
        output = stream.read()
        return output[:-1]
