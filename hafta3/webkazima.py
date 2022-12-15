"""
1. klavyeden bir anahtar kelime girilmesi istensin.
2. bu anahtar kelimeye göre google' da arama yapılsın.
    2.1. https://www.google.com/search?q=(girilen anahtar kelime)
    istekte bulunulacak. (requests) (web kazıma)
    2.2. istek sonucunda gelen cevap işlensin ve web sayfası başlıkları
    ekrana yazılsın (beatifulsoap) veri temizleme (data cleaning)

    pip install requests
    pip3 install requests
    py -m pip install request
    python -m pip install request
    pip install beautifulsoup4
"""
import requests
import bs4
sorgu = "mehmet"
data = requests.get("https://www.google.com/search?q="+sorgu)
# print(data.content)
"""
with open("sorgu.txt", "a") as f:
    f.write(data.text)
    f.close()
"""
soup = bs4.BeautifulSoup(data.content, 'html5lib')
# html5lib
table = soup.find_all('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'})
for k in table:
    print(k.text)
