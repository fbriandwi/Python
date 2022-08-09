# 1. menyambung string (concatenate)

nama_pertama = "Pep"
nama_tengah = "D"
nama_akhir = "Putra"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen karakter/string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status))

D = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1):" + nama_lengkap[-1]) # ngambil dari belakang
print("index ke-(0:2):" + nama_lengkap[0:3]) 
print("index ke-(4:10):" + nama_lengkap[4:11]) 

# item paling kecil 
print("paling kecil : " + min(nama_lengkap))
# item paling kecil 
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. opertator dalam bentuk methode

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + "=" + str(jumlah))