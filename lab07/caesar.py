import argparse
from cryptlib import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt a message using  a Caesar cipher."
    )

    action = parser.add_mutually_exclusive_group(required=True)

    action.add_argument(
        "-e",
        action="store_true",
        help="Encrypt the message."
    )

    action.add_argument(
        "-d",
        action="store_true",
        help="Decrypt the message."
    )

    action.add_argument(
        "-m",
        required=True,
        help="The message to encrypt or decrypt."
    )

    args = parser.parse_args()

    if args.e:
        result = encrypt(args.m, 3)
        print(result)
    else:
        result = decrypt(args.m, 3)
        print(result)

if __name__ == "__main__":
    main()