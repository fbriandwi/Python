data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")
print("\n")

list_2D = [data_0,data_1,6,9]
print(f"list 2D = {list_2D}")
print("\n")

# contoh penggunaan

peserta_0 = ["pep",22,"laki laki"]
peserta_1 = ["salma",21,"perempuan"]
peserta_2 = ["anjing",2,"laki laki"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"list peserta adalah = {list_peserta}")
print("\n")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")


# dengan reference

list_copy =  list_peserta.copy(); 
print(f"peserta  = {list_copy}")
peserta_0[0] = "gelas"
print(f"peserta  = {list_copy}")
print(f"peserta  = {list_peserta}")
