from onisleme import *

with open("SMSSpamCollection", "r") as dosya:
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

for i in range(len(mesajlar)):
    mesajlar[i] = convert_lower(mesajlar[i])
    mesajlar[i] = remove_punctuation(mesajlar[i])
    mesajlar[i] = remove_stop_words(mesajlar[i])
    mesajlar[i] = remove_small_length(mesajlar[i])
    mesajlar[i] = find_stems(mesajlar[i])

print(mesajlar[0])
find_word_count(etiketler, mesajlar)

spam_kelimeleri = ["free", "txt", "text",
                   "mobil"]
"""spam_sayac=0
for k in etiketler:
    if k=="spam":
        spam_sayac=spam_sayac+1
print(spam_sayac)
747
"""
bulunan_spam_sayac = 0
for mesaj in mesajlar:
    for s in spam_kelimeleri:
        if s in mesaj:
            bulunan_spam_sayac = bulunan_spam_sayac+1
            break
print(bulunan_spam_sayac)
# 10 kelime 1400
# 5 kelime 1047
