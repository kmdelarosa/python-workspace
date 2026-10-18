"""Password strength estimator."""
import string


def check_strength(password: str) -> str:
    """Return 'Weak', 'Medium', or 'Strong' based on password composition."""
    score = 0
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    if any(c in string.ascii_lowercase for c in password):
        score += 1
    if any(c in string.digits for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    return "Strong"
