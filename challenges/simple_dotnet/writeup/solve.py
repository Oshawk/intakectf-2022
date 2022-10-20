from base64 import b64decode

# From ILSpy:
bytes_ = "Not that easy sorry :(".encode()
array = bytes.fromhex("fb21bf9910fcf5a605234a91b536940724128c73ea4a")
array2 = b64decode("0yKq3h+hpbBHIh6GqXWGWDBTljLgHw==")

array3 = bytes(a ^ b ^ c for a, b, c in zip(bytes_, array, array2))

print(array3)
