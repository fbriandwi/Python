data = "ini adalah string"
print(data)
print(type(data))

# cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double qoute "..."
'''

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print('"hallo, apa kabar?"')
print("ini adalah hari jum'at")

# menggunakan tanda \
# membuat tanda | menjadi string
print('tidur saat jum\'atan')
print('how\'s your day?')

# backslash
print("C:\\user\\pep")

# tab
print("sia \tanjing, anjingnya jadi jauh")

# backspace
print("sia \banjing, anjingnya jadi deket")

# newline
print("baris pertama.\nbaris kedua.") # LF = line feed (unix, macos, linux)
print("baris pertama.\rbaris kedua.") # CR = carriage return (commodore, acorn, lisp)
print("baris pertama.\r\nbaris kedua.") # CRLF = line feed carriage return (dipakai oleh windows)

# string literal atau raw
# hati hati
# print('C:\new folder') akan salah pathnya
# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : pep
Kelas : berat
""")

# multiline literal string dan RAW
print(r"""
Nama : pep
Kelas : berat
Website : https://pep.co.id/newid
""")