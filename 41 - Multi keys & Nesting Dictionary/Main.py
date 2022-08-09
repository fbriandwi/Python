import datetime

mahasiswa1 = {
    'nama':'ucup surucup',
    'nim':'1104193095',
    'sks_lulus':144,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,2,16) # tahun,bulan,tanggal
}

mahasiswa2 = {
    'nama':'otong surotong',
    'nim':'1104193000',
    'sks_lulus':144,
    'beasiswa':True,
    'lahir':datetime.datetime(2001,10,14) # tahun,bulan,tanggal
}

mahasiswa3 = {
    'nama':'asep gojlag',
    'nim':'1104196969',
    'sks_lulus':144,
    'beasiswa':True,
    'lahir':datetime.datetime(2000,2,29) # tahun,bulan,tanggal
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("_"*50)

# kalo konstanta pake KEY
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

    
