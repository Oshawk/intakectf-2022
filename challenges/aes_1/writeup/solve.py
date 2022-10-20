from pwn import remote

io = remote("localhost", 42004)

io.sendlineafter(b"option: ", b"1")
io.sendlineafter(b"encrypt (hex): ", b"000000000000")

io.recvuntil(b"go: ")
nonce = bytes.fromhex(io.recv(16).decode())
ct = bytes.fromhex(io.recv(12).decode())

forged_ct = bytes(a ^ b for a, b in zip(ct, b"please"))

io.sendlineafter(b"option: ", b"2")
io.sendlineafter(b"check (hex): ", (nonce + forged_ct).hex().encode())

io.interactive()
