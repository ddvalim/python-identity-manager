from holder import anchor

def generate_did(seed):
    TRUST_ANCHOR = anchor.AnchorHandle()
    did, verkey = TRUST_ANCHOR.seed_to_did(seed)

    print(f"\nSeed: {seed}")
    print(f"DID: {did}")
    print(f"Verkey: {verkey}")

    return did, verkey