# LIST

#angka1 = 1
#angka2 = 2
#angka3 = 3

# kumpulan data numbers
from pickle import FALSE


data_angka = [1,2,3]
print(data_angka)
print("\n\n")

# kumpulan data string
data_string = ["febrian","dwi","putra"]
print(data_string)
print("\n\n")

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)
print("\n\n")

# kumpulan campuran
data_campuran = [1,"gehu",2,"cireng","pep",True,"dwi",False]
print(data_campuran)
print("\n\n")

## cara alternatif membuat list
data_range = range(0,10,2) #range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)
print("\n\n")

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)] # **2 buat kuadrat
print(list_pake_for)
print("\n\n")

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if) 

list_pake_for_if = [i for i in range(0,10) if i%2 ==0] # genap
print(list_pake_for_if) 

list_pake_for_if = [i for i in range(0,10) if i%2 !=0] # ganjil
print(list_pake_for_if) 