with open("sinav_veri_seti.txt", "r") as f:
    liste = f.readlines()
    f.close()


def change_label(label):
    if "#0#" in label:
        return "Olumsuz"
    elif "#1#" in label:
        return "Olumlu"
    else:
        return "Tarafsız"


etiketler = []
gorusler = []

for k in liste:
    if ";; " not in k:
        gorusler.append(k.split(";;")[0])
        etiketler.append(k.split(";;")[1])

with open("sinav_veri_seti_son.txt", "a") as f:
    for k in range(len(etiketler)):
        f.write(gorusler[k]+";;"+change_label(etiketler[k])+"\n")
    f.close()
