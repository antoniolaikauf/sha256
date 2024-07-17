from cryptography.hazmat.primitives import hashes

sha256=hashes.Hash(hashes.SHA256())
sha256.update(b'tutti')
print(sha256.finalize().hex(), 'parola come input "tutti"')

import hashlib

SHA256= hashlib.sha256()
SHA256.update(b'tutte')
print(SHA256.hexdigest(), 'parola come input "tutte"')