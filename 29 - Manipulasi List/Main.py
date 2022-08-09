# Operasi

# index 0(-3)  1(-2)  2(-1)
data = ["pep","dwi","putra"]

# mengambil data dari list

data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_pep = data[-3]
print(f"data pep = {data_pep}")
print("\n")

# mengambil info jumlah data dari list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")
print("\n\n")

## manipulasi data list

# menambahkan item pada list
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"obeng") #(posisi,item)
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("buku")
print(f"data sesudah ditambah lagi = \n {data}")
print("\n")

# menambah list dengan list
data_baru = ["anjing","goblog","setan"]
data.extend(data_baru)
print(f"data gabungan = \n {data}")
print("\n")

# merubah data
# kita ubah data 2 jadi jurig
data[2] = "jurig"
print(f"data rubah =  {data}")
print("\n")

# meremove data

data.remove("anjing")
print(f"data remove = \n {data}")
print("\n")

# meremove data paling belakang
data.pop() # pop menghapus data paling belakang
print(f"data akhir = \n {data}")
print("\n")
