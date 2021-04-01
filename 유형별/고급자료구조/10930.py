'''
SHA-256
'''

import hashlib

print(hashlib.sha256(input().encode()).hexdigest())
