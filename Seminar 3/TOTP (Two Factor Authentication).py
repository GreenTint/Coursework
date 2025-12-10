import pyotp
import qrcode

totp = pyotp.TOTP(pyotp.random_base32())
uri = totp.provisioning_uri(name="student@example.com", issuer_name="Week03Demo")

img = qrcode.make(uri)
img.save("totp_qr.png")

print("Scan totp_qr.png with your authenticator app.")
print("Current TOTP:", totp.now())
