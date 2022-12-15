print(type(1))  # int
print(type(1.9))  # float
print(type("k"))  # char
print(type("karakterdizisi"))  # str
print(type(True))  # bool
print(type([1, "asa", 3]))  # list
print(type((1, 2, 3)))  # tuple
print(type({1, 2, 3}))  # set
print(type({"adet": 1, "adet2": 3}))
"""
adem, aysen, ahmet, fikret

yukarıdaki isimlerden hangisi ayse ismine en çok
benzemektedir. Bu işlemi gerçekleştiren kodu yazınız.
"""
benzerlik = {"adem": 0, "şükran": 0, "ayfer": 0, "fikret": 0}
ayse = "ayse"
for index in range(len(ayse)):
    for anahtar, deger in benzerlik.items():
        if ayse[index] == anahtar[index]:
            benzerlik[anahtar] = benzerlik[anahtar]+1

print(benzerlik)
