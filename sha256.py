'''
sha256 with module
'''
words=b'ciao'
from cryptography.hazmat.primitives import hashes

sha256=hashes.Hash(hashes.SHA256())
sha256.update(words)
print(sha256.finalize().hex(), f'parola come input "ciao"')

import hashlib

SHA256= hashlib.sha256()
SHA256.update(words)
print(SHA256.hexdigest(), 'parola come input "ciao"')