# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 #adalah assignment
print("nilai a =",a)

a += 1  # sama aja kaya a = a + 1
print("nilai a += 1, nilai a menjadi",a)

a -= 2 # a = a - 2
print("nilai a -= 2, nilai a menjadi",a)

a *= 5 # a = a * 5
print("nilai a *= 5, nilai a menjadi",a)

a /= 2 # a = a / 2
print("nilai a /= 2, nilai a menjadi",a)

b = 10
print("\nnilai b =",b)

# modulus dan floor division
b %= 3
print("nilai b %= 3, nilai b menjadi",b)

b = 10
print("\nnilai b =",b)

b //= 3
print("nilai b //= 3, nilai b menjadi",b)

# eksponen atau pangkat
a = 5
print("nilai a =",a)
a **= 3
print("nilai a **= 3, nilai a menjadi",a)

# operasi bitwise
# OR 
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)
 
c = False
print("nilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

# OR 
print("=====OR=====")
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)
 
c = False
print("nilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

# AND
print("=====AND=====")
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, nilai c menjadi",c)
 
c = True
print("nilai c =",c)
c &= True
print("nilai c &= True, nilai c menjadi",c)

# XOR
print("=====XOR=====")
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= False, nilai c menjadi",c)
 
c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= True, nilai c menjadi",c)

# geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2 
print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1 
print("nilai d <<= 1, nilai d menjadi",format(d,'04b'))