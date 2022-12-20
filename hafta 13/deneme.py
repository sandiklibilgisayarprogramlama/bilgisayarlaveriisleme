# pip install -U scikit-learn
# Öncelikle gerekli kütüphanelerin içe aktarılması
from sklearn.naive_bayes import GaussianNB

"""
Göz rengi - boy - gözlük durum - saç-rengi -     Kız? erkek?
 siyah  0     160       var 0          siyah 0      kız   0
 yeşil  1     170       yok 1          sarı  1      erkek 1
 siyah  0     180       var 0          siyah 0      erkek 1
 mavi   2     170       yok 1          siyah 0      erkek 1
 yeşil  1     150       var 0          siyah 0      kız   0
 kahve  3     160       yok 1          sarı  1      kız   0
 siyah  0     165       var 0          siyah 0      erkek 1

 siyah  0      175      yok 1          sarı  1       ?
"""

# Veri kümesi oluşturulur
X = [[0, 160, 0, 0], [1, 170, 1, 1], [0, 180, 0, 0], [
    2, 170, 1, 0], [1, 150, 0, 0], [3, 160, 1, 1], [0, 165, 0, 0]]
y = [0, 1, 1, 1, 0, 0, 1]

# Naive Bayes modeli oluşturulur
model = GaussianNB()
# Model eğitilir
model.fit(X, y)
# Model test edilir
y_pred = model.predict([[0, 175, 1, 1]])

# Test sonuçları yazdırılır
print(y_pred)
