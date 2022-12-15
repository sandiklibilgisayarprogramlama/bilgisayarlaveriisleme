x = [20, 21, 23, 26]
y = [6000, 8000, 9000, 12000]

# y = a*x+b
eleman_say = len(x)
x_toplam = sum(x)
y_toplam = sum(y)

x2_toplam = 0
xy_toplam = 0
for i in range(len(x)):
    xy_toplam += x[i]*y[i]
    x2_toplam += x[i]**2

# print(x_toplam)
# print(x2_toplam)
# print(xy_toplam)
# print(y_toplam)

b = ((eleman_say*xy_toplam)-(x_toplam*y_toplam)) / \
    ((eleman_say*x2_toplam)-(x_toplam**2))
print(b)
a = y[0]-x[0]*b
print(a)  # y = b*x+a
print("30 yaşında kazanacağı")
print(b*30+a)
