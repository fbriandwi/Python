# operator dalam bentuk methods

## merubah case dari string

#merubah semua ke upper case

from ntpath import join


salam = "anjing!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
contoh = "aKu GanTenGzzZ"
print("contoh = " + contoh)
contoh = contoh.lower()
print("lower =" + contoh)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "halloo"
apakah_lower = salam.islower() # hasilnya bool jadi harus pake str
print(salam +" is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool jadi harus pake str
print(salam +" is upper = " + str(apakah_upper))

# isalpha() = untuk mengecek semuanya huruf
# isalnum() = huruf dan angka
# isdecimal() = untuk angka saja
# isspace() = spasi, tab, newline \n
# istitle() = semua kata dimulai dengan huruf besar
# capitalize() = Mengubah Kata yang huruf depannya lowercase jadi uppercase

judul = "It Is Okat Not To Be Okay"
cek_judul = judul.istitle() # hasilnya bool
print(judul + " is title? " + str(cek_judul)) 

## ngecek komponen startwith() endswith()
cek_start = "Dasar Anjing".startswith("Dasar")
print("start = " + str(cek_start))

cek_end = "Dasar Anjing".endswith("Anjing")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'anjing']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = ' '.join(pisah)
print(gabungan) 

gabungan = ' ehm '.join(pisah)
print(gabungan) 

gabungan = "akuehmsayangehmanjing"
print(gabungan.split('ehm'))

# alokasi karakter rjust(),  ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikan = strip()
tengah = tengah.strip("-") # menghilangkan tanda -
print("'"+tengah+"'")