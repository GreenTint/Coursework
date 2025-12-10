import string
import math

COMMON_PASSWORDS = {"password", "123456", "qwerty", "pass123", "letmein"}

def password_strength(password: str):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (minimum 8).")

    if len(password) >= 12:
        score += 1

    # Character sets
    pool = 0
    if any(c.islower() for c in password):
        score += 1
        pool += 26
    if any(c.isupper() for c in password):
        score += 1
        pool += 26
    if any(c.isdigit() for c in password):
        score += 1
        pool += 10
    if any(c in string.punctuation for c in password):
        score += 1
        pool += len(string.punctuation)

    # Common password
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Password is too common.")

    # Entropy
    entropy = len(password) * math.log2(pool) if pool > 0 else 0

    return {
        "score": score,
        "entropy": round(entropy, 2),
        "feedback": feedback
    }

# Test
for pw in ["Pass123", "MyP@ssw0rd", "CorrectHorseBatteryStaple!"]:
    print(pw, password_strength(pw))
