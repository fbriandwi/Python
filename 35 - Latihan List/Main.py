# program list buku

list_buku = []
while True:
    print("masukan data buku")
    judul = input("judul buku\t : ")
    penulis = input("nama penulis\t : ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("no. \t| judul\t\t| penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}\t|{buku[0]}\t\t| {buku[1]}")

    print("\n\n","="*20)
    isLanjut = input("apakah dilanjutkan?(y/n) ")
    if isLanjut == "n":
        break
print("program selesai")