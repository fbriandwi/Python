# width and multiline

# Data

data_nama = "Gol Roger"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter atau \n)
data_string = f"nama = {data_nama} \numur = {data_umur} \ntinggi = {data_tinggi} \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline pakai kutip triplets

data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggu = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Nami"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggu = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)