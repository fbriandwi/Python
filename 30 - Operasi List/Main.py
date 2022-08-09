data_angka = [1,2,5,3,5,4,7,3,5,6,2,4,2]

print(f"data angka = {data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["pep","dwi","putra"]
print(f"data = {data}")

index_putra = data.index("putra")
index_pep = data.index("pep")
print(f"index si putra  = {index_putra}")
print(f"index si pep  = {index_pep}")
print("\n")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")
print("\n")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data direverse = \n{data_angka} \n{data}")