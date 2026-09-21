"""Chunked, authenticated encryption for offsite backups.

A file is read in CHUNK_BYTES pieces; each piece becomes one Fernet token
(AES-128-CBC + HMAC-SHA256). Tokens are uploaded and stored separately,
so a multi-gigabyte backup never has to sit in memory, and a tampered or
truncated chunk fails loudly on restore. The key never leaves the install.
"""

import hashlib

from cryptography.fernet import Fernet, InvalidToken

CHUNK_BYTES = 8 * 1024 * 1024


def new_key() -> str:
	return Fernet.generate_key().decode()


def encrypted_chunks(path: str, key: str):
	"""Yield (index, token bytes) for each CHUNK_BYTES piece of the file."""
	f = Fernet(key.encode())
	with open(path, "rb") as fh:
		index = 0
		while True:
			block = fh.read(CHUNK_BYTES)
			if not block:
				break
			yield index, f.encrypt(block)
			index += 1


def file_sha256(path: str) -> str:
	h = hashlib.sha256()
	with open(path, "rb") as fh:
		for block in iter(lambda: fh.read(CHUNK_BYTES), b""):
			h.update(block)
	return h.hexdigest()


def decrypt_chunk(token: bytes, key: str) -> bytes:
	try:
		return Fernet(key.encode()).decrypt(token)
	except InvalidToken as e:
		raise ValueError("Backup chunk failed to decrypt: wrong recovery key or damaged data") from e
