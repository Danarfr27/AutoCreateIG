# Copy-paste this to generate a TOTP locally (Python 3).
import time, hmac, hashlib, struct
secret = bytes.fromhex("70e57a875370361611249adc097dfe7695042c24")
def totp(secret, digits=6, timestep=30):
    t = int(time.time())
    counter = int(t // timestep)
    msg = struct.pack(">Q", counter)
    h = hmac.new(secret, msg, hashlib.sha1).digest()
    offset = h[-1] & 0x0F
    code = struct.unpack(">I", h[offset:offset+4])[0] & 0x7FFFFFFF
    return str(code % (10 ** digits)).zfill(digits)
print("TOTP (6):", totp(secret, 6))
print("TOTP (8):", totp(secret, 8))
