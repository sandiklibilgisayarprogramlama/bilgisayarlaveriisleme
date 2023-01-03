import re

liste = []
with open("magaza_yorumlari_duygu_analizi (1).csv", "r", encoding='utf-16') as f:
    liste = f.readlines()
    f.close()

metin = ""
for satir in liste:
    metin += satir

metin = metin.replace("\n", "")
metin = metin.replace(",Olumsuz", "#0#")
metin = metin.replace(",Olumlu", "#1#")
metin = metin.replace(",Tarafsız", "#2#")
# print(metin)

spt = re.split("#[0-2]#", metin)
etiketler = []

for gorus in spt:
    inx = metin.find(gorus)
    etiketler.append(metin[inx+len(gorus):inx+len(gorus)+3])

with open("sinav_veri_seti.txt", "a") as f:
    for k in range(len(spt)):
        f.write(spt[k]+";;"+etiketler[k]+"\n")
    f.close()
