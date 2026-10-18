"""Entry point for the Password Generator."""
import argparse
from generator import generate_passwords
from strength import check_strength


def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    parser.add_argument("--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("--count", type=int, default=1, help="Number of passwords (default: 1)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    args = parser.parse_args()

    config = {
        "length": args.length,
        "upper": not args.no_upper,
        "lower": not args.no_lower,
        "digits": not args.no_digits,
        "symbols": not args.no_symbols,
    }

    passwords = generate_passwords(config, args.count)
    for pwd in passwords:
        strength = check_strength(pwd)
        print(f"{pwd}  [{strength}]")


if __name__ == "__main__":
    main()
