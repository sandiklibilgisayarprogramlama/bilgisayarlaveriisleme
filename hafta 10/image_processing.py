# image processing -> görüntü işleme

# pip install opencv-python

import cv2

image = cv2.imread("aku_logo.png", cv2.IMREAD_GRAYSCALE)
#image2 = cv2.imread("bg.png")
# print(image.shape)  # (yükseklik,genişlik)
# print(image[200][100]) # belirli bir piksel değeri getirir.
# image = cv2.addWeighted(image, 0.8, image2, 0.2, 0)
# image -> matris(RGB)(yukseklik, genislik, 3)
# image -> matris(gri veya binary)(yukseklik, genislik)
output2 = cv2.blur(image, (10, 10))
#cv2.imshow('Resim', image)
cv2.imshow('Resim', output2)
cv2.waitKey(0)

# print(image)
