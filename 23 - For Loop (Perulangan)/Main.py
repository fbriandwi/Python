# perulangan (loop)

# contoh
#angka = 1
#print(angka)
#angka = angka+ 1
#print(angka)
#angka = angka + 1
#print(angka)

# for kondisi:
#    aksi

# ini dengan list
angka2_list = [0,2,4,8,10] # ini adalah list
print(angka2_list)

for i in angka2_list:
    print(f"i sekarang = {i}")

print("akhir dari program 1\n")

# ini adalah range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang = {i}")

print("akhir dari program 2\n")

angka2_range = range(1,5)

for i in angka2_range:
    print(f"i sekarang = {i}")

print("akhir dari program 3\n")

# menggunakan string

data_str = "bengeut jiga monyet"

for huruf in data_str:
    print(huruf)

print("akhir dari program 3\n")

#for(int i=1; i<10;i++){
#    i = 1 + 1
#    print(i)
#}