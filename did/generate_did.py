import logging
import sys

# Import server.anchor from the path relative to where the scripts are being executed.
sys.path.insert(1, './server')
from holder import anchor

logging.getLogger().setLevel(logging.ERROR)

async def generate_did(seed):
    TRUST_ANCHOR = anchor.AnchorHandle()
    did, verkey, x = await TRUST_ANCHOR.seed_to_did(seed)

    print(f"\nSeed: {seed}")
    print(f"DID: {did}")
    print(f"Verkey: {verkey}")

    return did, verkey