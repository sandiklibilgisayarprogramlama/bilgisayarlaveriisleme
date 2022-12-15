from string import punctuation
print("aD".index("D"))  # kaçıncı indexte
print("a".isalpha())  # karakter kontrol
print("a12".isalnum())  # sayı veya karakter kontrol
print("12".isdecimal())  # sayı kontrol
print("1".isdigit())  # rakam kontrol
print("u".islower())  # harfler kuçuk mu
print("U".isupper())  # harfler buyuk mu
print("      ".isspace())
print("Naber Napıyorsun".istitle())
print(" dasd ".strip())
# karakter dizisinin sonundaki ve başında boş karakterleri siler
if "ahmet" == "  ahmet  ".strip():
    print(True)
else:
    print(False)
print(ord(" "))  # ascii kod bulma

print("  selam naber   ")
print("  selam naber   ".strip())  # strip aradaki boşlukları kaldırmaz.

"""
strip fonksiyonunun görevini yapan fonksiyonu yazınız.
"""

print("555h5f5s555a".count("a"))  # parametre olarak verilen karakterin
# cümlede ne kadar
# geçtigini verir.

print("ahmet".endswith("t"))  # cümlenin parametre olarak verilen ifadeyle
# bitip bitmediğini söyler.

print("veli naber".replace("veli", "ayşe"))
# parametre olarak verilen ifadeleri cümlede yer değiştirir

print("   ahmet    ".strip())
print("   ahmet    ".replace(" ", "_"))

print("ahmet".startswith("ah"))
# parametre olarak verilen ifade ile cümlenin başlayıp başlamadığı
# kontrolü

print("ferdi".find("er"))
# parametre olarak verilen ifade cümlede var ise indeksi geriye döner.
# yok ise geriye -1 döndürür.

print("ahmet selam naber arkadaşım".split(" "))
print("ali,veli,49,50".split(","))
# seperator -> ayraç belirli bir ayraça göre ifadeyi bölüp liste oluşturur.

for harf in "ahmet":
    print(harf)

print(list("ahmet"))
"""
Ali, bakkaldan süt almaya gitti.
Ali bakkala süt almak için gitti.
Süt almak için bakkala gidiyor ali.

1- tüm harflerin küçültülmesi
2- noktalama işaretlerinin kaldırılması
3- bağlaçların kaldırılması, ve veya için de da
4- sık kullanılan ozneler yüklem vb. ifadeler
5- kök bulma

ali bakkal süt al git
ali bakkal süt al git
süt al bakkal git ali

"""


def convert_lower(input):
    return input.lower()


def remove_punctuation(input):
    for p in punctuation:
        input = input.replace(p, "")
    return input


cumle1 = "Ali, bakkaldan süt almaya gitti."
cumle2 = "Ali bakkala süt almak için gitti."
cumle3 = "Süt almak için bakkala gidiyor ali."

cumle1_1 = convert_lower(cumle1)
cumle2_1 = convert_lower(cumle2)
cumle3_1 = convert_lower(cumle3)

cumle1_2 = remove_punctuation(cumle1_1)
cumle2_2 = remove_punctuation(cumle2_1)
cumle3_2 = remove_punctuation(cumle3_1)

print(cumle1_2)
print(cumle2_2)
print(cumle3_2)
print("------------------------------")

# "ahmet naber".split(" ") # ["ahmet","naber"]
# " ".join(["ahmet","naber"]) # ahmet naber


def remove_stop_words(input):
    stop_words = ['a', 'acaba', 'altı', 'altmış', 'ama', 'ancak', 'arada', 'artık', 'asla', 'aslında', 'aslında', 'ayrıca', 'az', 'bana', 'bazen', 'bazı', 'bazıları', 'belki', 'ben', 'benden', 'beni', 'benim', 'beri', 'beş', 'bile', 'bilhassa', 'bin', 'bir', 'biraz', 'birçoğu', 'birçok', 'biri', 'birisi', 'birkaç', 'birşey', 'biz', 'bizden', 'bize', 'bizi', 'bizim', 'böyle', 'böylece', 'bu', 'buna', 'bunda', 'bundan', 'bunlar', 'bunları', 'bunların', 'bunu', 'bunun', 'burada', 'bütün', 'çoğu', 'çoğunu', 'çok', 'çünkü', 'da', 'daha', 'dahi', 'dan', 'de', 'defa', 'değil', 'diğer', 'diğeri', 'diğerleri', 'diye', 'doksan', 'dokuz', 'dolayı', 'dolayısıyla', 'dört', 'e', 'edecek', 'eden', 'ederek', 'edilecek', 'ediliyor', 'edilmesi', 'ediyor', 'eğer', 'elbette', 'elli', 'en', 'etmesi', 'etti', 'ettiği', 'ettiğini', 'fakat', 'falan', 'filan', 'gene', 'gereği', 'gerek', 'gibi', 'göre', 'hala', 'halde', 'halen', 'hangi', 'hangisi', 'hani', 'hatta', 'hem', 'henüz', 'hep', 'hepsi', 'her', 'herhangi', 'herkes', 'herkese', 'herkesi', 'herkesin', 'hiç', 'hiçbir', 'hiçbiri', 'i', 'ı', 'için', 'içinde', 'iki', 'ile', 'ilgili', 'ise', 'işte', 'itibaren', 'itibariyle', 'kaç', 'kadar', 'karşın', 'kendi', 'kendilerine', 'kendine', 'kendini', 'kendisi', 'kendisine', 'kendisini',
                  'kez', 'ki', 'kim', 'kime', 'kimi', 'kimin', 'kimisi', 'kimse', 'kırk', 'madem', 'mi', 'mı', 'milyar', 'milyon', 'mu', 'mü', 'nasıl', 'ne', 'neden', 'nedenle', 'nerde', 'nerede', 'nereye', 'neyse', 'niçin', 'nin', 'nın', 'niye', 'nun', 'nün', 'o', 'öbür', 'olan', 'olarak', 'oldu', 'olduğu', 'olduğunu', 'olduklarını', 'olmadı', 'olmadığı', 'olmak', 'olması', 'olmayan', 'olmaz', 'olsa', 'olsun', 'olup', 'olur', 'olur', 'olursa', 'oluyor', 'on', 'ön', 'ona', 'önce', 'ondan', 'onlar', 'onlara', 'onlardan', 'onları', 'onların', 'onu', 'onun', 'orada', 'öte', 'ötürü', 'otuz', 'öyle', 'oysa', 'pek', 'rağmen', 'sana', 'sanki', 'sanki', 'şayet', 'şekilde', 'sekiz', 'seksen', 'sen', 'senden', 'seni', 'senin', 'şey', 'şeyden', 'şeye', 'şeyi', 'şeyler', 'şimdi', 'siz', 'siz', 'sizden', 'sizden', 'size', 'sizi', 'sizi', 'sizin', 'sizin', 'sonra', 'şöyle', 'şu', 'şuna', 'şunları', 'şunu', 'ta', 'tabii', 'tam', 'tamam', 'tamamen', 'tarafından', 'trilyon', 'tüm', 'tümü', 'u', 'ü', 'üç', 'un', 'ün', 'üzere', 'var', 'vardı', 've', 'veya', 'ya', 'yani', 'yapacak', 'yapılan', 'yapılması', 'yapıyor', 'yapmak', 'yaptı', 'yaptığı', 'yaptığını', 'yaptıkları', 'ye', 'yedi', 'yerine', 'yetmiş', 'yi', 'yı', 'yine', 'yirmi', 'yoksa', 'yu', 'yüz', 'zaten', 'zira', 'zxtest']
    input_list = input.split(" ")
    for w in stop_words:
        if w in input_list:
            input_list.remove(w)

    return " ".join(input_list)


cumle1_3 = remove_stop_words(cumle1_2)
cumle2_3 = remove_stop_words(cumle2_2)
cumle3_3 = remove_stop_words(cumle3_2)

print(cumle1_3)
print(cumle2_3)
print(cumle3_3)

# stop word (durak kelime) bir cümleden çıkarıldığı zaman
# cümle anlamını en az derecede değiştiren kelimeler
# topluluğudur.
"""

pip install TurkishStemmer
pip3 install TurkishStemmer
py -m pip install TurkishStemmer
python -m pip install TurkishStemmer
"""


def find_stem(input):
    from snowballstemmer import TurkishStemmer
    input_list = input.split(" ")
    stemmer = TurkishStemmer()
    new_list = []
    for s in input_list:
        new_list.append(stemmer.stemWord(s))
    return list(set(new_list))


cumle1_son = find_stem(cumle1_3)
cumle2_son = find_stem(cumle2_3)
cumle3_son = find_stem(cumle3_3)

print(cumle1_son)
print(cumle2_son)
print(cumle3_son)
