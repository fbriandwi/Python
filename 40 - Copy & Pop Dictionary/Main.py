# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep anjing",
    "cuy":"ucuy goblog"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}")
print(f"friends: {friends}")

teman_teman["cup"] = "ucup anjing juga"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir aja)
dataterakhir = friends.popitem()
print(f"data terakhir = {dataterakhir}\n")
print(f"friends = {friends}\n")
