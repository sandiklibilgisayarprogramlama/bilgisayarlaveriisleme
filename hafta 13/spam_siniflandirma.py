from sklearn.naive_bayes import GaussianNB
with open("SMSSpamCollection.txt", "r") as dosya:
    belge_liste = dosya.readlines()
    dosya.close()

etiketler = []
mesajlar = []

for mesaj in belge_liste:
    bolunmus_mesaj = mesaj.split("\t")
    etiketler.append(bolunmus_mesaj[0])
    mesajlar.append(bolunmus_mesaj[1])

print(etiketler[0])
print(mesajlar[0])

kelimeler = ["free", "txt", "text",
             "mobil", 'you', 'get', 'come', 'call', 'dont']

X = []
y = []

for index in range(len(mesajlar)):
    mesaj = mesajlar[index].lower()
    x_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for kelime in kelimeler:
        if kelime in mesaj:
            if kelime == "free":
                x_vector[0] = 1
            if kelime == "txt":
                x_vector[1] = 1
            if kelime == "text":
                x_vector[2] = 1
            if kelime == "mobil":
                x_vector[3] = 1
            if kelime == "you":
                x_vector[4] = 1
            if kelime == "get":
                x_vector[5] = 1
            if kelime == "come":
                x_vector[6] = 1
            if kelime == "call":
                x_vector[7] = 1
            if kelime == "dont":
                x_vector[8] = 1
    X.append(x_vector)

    if etiketler[index] == "ham":
        y.append(0)
    else:
        y.append(1)

ornek_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ornek = "Hello yusuf, how ar you ?"
for kelime in kelimeler:
    if kelime in ornek.lower():
        if kelime == "free":
            ornek_vector[0] = 1
        if kelime == "txt":
            ornek_vector[1] = 1
        if kelime == "text":
            ornek_vector[2] = 1
        if kelime == "mobil":
            ornek_vector[3] = 1
        if kelime == "you":
            ornek_vector[4] = 1
        if kelime == "get":
            ornek_vector[5] = 1
        if kelime == "come":
            ornek_vector[6] = 1
        if kelime == "call":
            ornek_vector[7] = 1
        if kelime == "dont":
            ornek_vector[8] = 1
print(ornek_vector)

# Naive Bayes modeli oluşturulur
model = GaussianNB()
# Model eğitilir
model.fit(X, y)
# Model test edilir
y_pred = model.predict([ornek_vector])

# Test sonuçları yazdırılır
print(y_pred)
