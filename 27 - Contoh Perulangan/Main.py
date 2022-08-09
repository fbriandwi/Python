# latihan perulangan membuat segitiga

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

sisi = 10

# 1. menggunakan for

# dummy variable
print("awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for\n\n")

# 2. menggunakan while
print("awal dari while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir dari while\n\n")


# 3. hanya ganjil saja
print("hanya ganjil saja")
count = 1
while True:
	if (count%2):
		# Print jika ganjil
		print("*"*count)
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier dari hanya ganjil saja\n\n")

# 4. hanya ganjil saja part 2
print("hanya ganjil saja part 2")
count = 1
spasi = int(sisi/2)

while True:
	if (count%2):
		# Print jika ganjil
		print(" "*spasi,"+"*count)
		spasi -= 1
		count += 1
	else:
		# akan kembali ke atas jika ganjil
		count += 1
		continue

	# akan break jika count melebihi sisi
	if count > sisi:
		break

print("akhier dari hanya ganjil saja part 2\n\n")
