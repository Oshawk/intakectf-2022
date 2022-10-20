from random import randbytes

from Crypto.Cipher import AES

KEY = randbytes(16)
FLAG = open("flag.txt").read()


def encrypt():
    pt = bytes.fromhex(input("Enter the plaintext you want to encrypt (hex): "))

    if any(i in pt for i in b"please"):
        print("It's not that easy.")
        return

    aes = AES.new(KEY, AES.MODE_CTR)
    ct = aes.encrypt(pt)

    print(f"Here you go: {(aes.nonce + ct).hex()}")


def check():
    ct = bytes.fromhex(input("Enter the ciphertext you want to check (hex): "))

    aes = AES.new(KEY, AES.MODE_CTR, nonce=ct[:8])
    pt = aes.decrypt(ct[8:])

    if b"please" in pt:
        print(f"Here is the flag: {FLAG}")
        exit()
    else:
        print("Decrypted plaintext did not include the magic word.")


def main():
    while True:
        try:
            print("1. Encrypt")
            print("2. Check")
            print("3. Exit")
            option = int(input("Choose an option: "))

            assert option in (1, 2, 3)

            if option == 1:
                encrypt()
            elif option == 2:
                check()
            else:
                exit()
        except Exception:
            print("Something went wrong...")


if __name__ == '__main__':
    main()
