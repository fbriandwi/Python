# date and time (latihan)

import datetime as dt

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_hari_sisa = (umur_hari.days % 30)

print(umur_hari)
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_hari_sisa} hari")