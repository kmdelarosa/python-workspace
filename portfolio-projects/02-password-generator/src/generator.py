"""Password generation using the secrets module."""
import secrets
import string


def generate_passwords(config: dict, count: int = 1) -> list[str]:
    """Generate `count` passwords based on the given config."""
    charset = _build_charset(config)
    if not charset:
        raise ValueError("At least one character type must be enabled.")

    return ["".join(secrets.choice(charset) for _ in range(config["length"])) for _ in range(count)]


def _build_charset(config: dict) -> str:
    charset = ""
    if config.get("upper"):
        charset += string.ascii_uppercase
    if config.get("lower"):
        charset += string.ascii_lowercase
    if config.get("digits"):
        charset += string.digits
    if config.get("symbols"):
        charset += string.punctuation
    return charset
