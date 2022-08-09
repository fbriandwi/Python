# looping dari list

# for loop
print("ini adalah for loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["pep","dwi","putra","anjing","goblog"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nini adalah for loop dan range")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")


#while
print("\nini adalah while loop")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# menggunakan list comprehension
print("\nini adalah list comprehension")

data = ["pep",1,2,3,"anjing"]

[print(f"data = {i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nini adalah enumerate")
data_list = ["pep",1,2,3,"anjing"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")