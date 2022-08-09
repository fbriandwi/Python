# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong sorotong",
    "dung":"dudung surudung"
}

# panjang dictionary
lendict = len(data_dict)
print(f"panjang dari dictionary : {lendict}")

#  mengecek key exist atau tidak
key = "cup"
checkkey =  key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("cuy","key tidak ditemukan")) # kalo gapake get malah error

# mengupdate data
data_dict["cup"] = "ucup anjing"
print(data_dict)
data_dict["sep"] = "asep goblog"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"pep":"pep dewa hs"}) # kalo gaada di add aja
print(data_dict)

# mendelete data pada dictionary
del data_dict["pep"]
print(data_dict)