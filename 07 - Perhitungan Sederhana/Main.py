# program konversi celcius ke satuan lain

print("PROGRAM KONVERSI TEMPRATUR\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah",celcius, "celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur",reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit",fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin",kelvin, "kelvin")

fahrenheit = float(input('Masukkan Suhu dalam Fahrenheit: '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin)

kelvin = float(input('Masukkan suhu dalam kelvin: '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit:", fahrenheit)