import bcrypt
import pyotp

class AuthSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        totp_secret = pyotp.random_base32()
        self.users[username] = {
            "password": pw_hash,
            "totp": totp_secret
        }
        print("User registered.")
        return pyotp.TOTP(totp_secret).provisioning_uri(
            name=username,
            issuer_name="AuthSystem"
        )

    def authenticate(self, username, password, otp):
        user = self.users.get(username)
        if not user:
            return False

        if not bcrypt.checkpw(password.encode(), user["password"]):
            return False

        totp = pyotp.TOTP(user["totp"])
        return totp.verify(otp)

# Demo
auth = AuthSystem()
uri = auth.register_user("alice", "StrongP@ssword123")
print("Scan QR URI:", uri)
