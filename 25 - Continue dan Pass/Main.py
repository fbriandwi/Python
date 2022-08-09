# continue, pass, break

# pass = berfungi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:

    angka += 1
    if angka == 3:
        # print("waduuh") bisa pake gitu jadi angka 3nya keganti
        pass # ini tidak akan dieksekusi

    print(angka)
print("\n\n")

# continue 

angka = 0

print(f"angka sekarang = {angka}") 

while angka < 5:
    angka += 1
    print(f"angka sekarang = {angka}") # aksi 1

    if angka == 3:
        print("nice")
        continue # akan membuat loop meloncat

    print("hallo") # aksi 2

print("finish")

