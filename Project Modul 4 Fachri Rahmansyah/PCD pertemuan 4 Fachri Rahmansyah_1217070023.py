Latihan Pertemuan 4
1. Split RGB channels & Merges different channels
# Fachri Rahmansyah
# 1217070023 PCD TSEB
import cv2
import numpy as np

image = cv2.imread("nurhadi.jpg")
b,g,r = cv2.split(image)
# Buat matriks seukuran dengan citra
matriks0 = np.zeros(image.shape[:2],image.dtype)
m = matriks0
# Merge matriks dengan matriks citra channel merah
merah = cv2.merge([m,m,r])
cv2.imshow('Citra red channel', merah)
cv2.waitKey(0)

2.Operasi Negatif
# Fachri Rahmansyah
# 1217070023 PCD TSEB
import cv2
import numpy as np

image = cv2.imread("nurhadi.jpg")

# Maksimum Pixel
max_pixel_value = 255
# Rumus citra negatif 255 - f(x,y)
inverted_image = max_pixel_value - image

cv2.imshow('Original image', image)
cv2.imshow('Citra negatif', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

3. Image Brightening
# Fachri Rahmansyah
# 1217070023 PCD TSEB
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("nurhadi.jpg")
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

# Melakukan penambahan brightness dengan nilai
img_brightness = np.zeros(img.shape, dtype=np.uint8)
def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)

brighter(-100)
plt.imshow(img_brightness)
plt.title("Brightness -100")
plt.show()

brighter(100)
plt.imshow(img_brightness)
plt.title("Brightness 100")
plt.show()

4. Penjumlahan
# Fachri Rahmansyah
# 1217070023 PCD TSEB
import cv2
import numpy as np

image = cv2.imread("nurhadi.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2],image.dtype)*100

# Operasi Penjumlahan
citraPenjumlahan = cv2.add(gray,MatriksSatu)
cv2.imshow('Citra', gray)
cv2.imshow('Citra Penjumlahan', citraPenjumlahan)
cv2.waitKey(0)

### Penjumlahan Manual ###
# Fachri Rahmansyah
# 1217070023 PCD TSEB
import cv2

# membaca dua gambar
gambar1 = cv2.imread('nurhadi.jpg')
gambar2 = cv2.imread('gambar.jpg')

# Operasi Penjumlahan
tinggi, lebar, _ = gambar1.shape
gambar2 = cv2.resize(gambar2, (lebar, tinggi))

tinggi, lebar, _ = gambar1.shape
gambar2 = cv2.resize(gambar2, (lebar, tinggi))

hasil_penjumlahan = gambar1.copy()

for y in range(tinggi):
    for x in range(lebar):
        for c in range(3):
            nilai_baru = gambar1[y, x, c] + gambar2[y, x, c]
            hasil_penjumlahan[y, x, c] = min(nilai_baru,255)

cv2.imshow('Hasil Penjumlahan', hasil_penjumlahan)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('hasil_penjumlahan_manual_rumus.jpg', hasil_penjumlahan)

## 5.A operasi boolean operator AND
# Fachri Rahmansyah
# 1217070023 PCD TSEB

import cv2
import numpy as np

persegi = np.zeros( (400,400) ,dtype="uint8")
cv2.rectangle(persegi, (60,60) , (340,340) ,255, -1)
lingkaran = np.zeros( (400,400) ,dtype="uint8")
cv2.circle(lingkaran, (200,200) ,150,255,-1)
operasiAND = cv2.bitwise_and(persegi, lingkaran)
cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi AND", operasiAND)
cv2.waitKey(0)

## 5. B operasi boolean operator OR
# Fachri Rahmansyah
# 1217070023 PCD TSEB

import cv2
import numpy as np

persegi = np.zeros( (400,400) ,dtype="uint8")
cv2.rectangle(persegi, (60,60) , (340,340) ,255, -1)
lingkaran = np.zeros((400,400) ,dtype="uint8")
cv2.circle(lingkaran, (200,200) ,150,255,-1)
operasiOR = cv2.bitwise_or(persegi, lingkaran)
cv2.imshow("Persegi", persegi)
cv2.imshow("“Lingkaran", lingkaran)
cv2.imshow("“Operasi Or", operasiOR)
cv2.waitKey(0)

##5. C operasi boolean operator XOR
# Fachri Rahmansyah
# 1217070023 PCD TSEB

import cv2
import numpy as np

persegi = np.zeros( (400,400) ,dtype="uint8")
cv2.rectangle(persegi, (60,60) , (340,340) ,255, -1)
lingkaran = np.zeros( (400,400) ,dtype="uint8")
cv2.circle(lingkaran, (200,200) ,150,255,-1)
operasiXOR = cv2.bitwise_xor(persegi, lingkaran)
cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi Xor", operasiXOR)
cv2.waitKey(0)

##5. D operasi boolean operator NOT
# Fachri Rahmansyah
# 1217070023 PCD TSEB

import cv2
import numpy as np

persegi = np.zeros( (400,400) ,dtype="uint8")
cv2.rectangle(persegi, (60,60) , (340,340) ,255, -1)
lingkaran = np.zeros( (400,400) ,dtype="uint8")
cv2.circle(lingkaran, (200,200) ,150,255,-1)
operasiNOT= cv2.bitwise_not(persegi)
cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi Not", operasiNOT)
cv2.waitKey(0)

## 6. A Operasi Geometri - Operasi Translasi
# Fachri Rahmansyah
# 1217070023 PCD TSEB

import cv2
import numpy as np
image = cv2.imread('images.jpg')
height, width = image.shape[:2]
M = np.float32([[1,0,100], [0,1,50]])
image_translation = cv2.warpAffine(image, M,(height, width))
cv2.imshow('Citra', image)
cv2.imshow('Citra Hasil Translasi', image_translation)
cv2.waitKey(0)

## 6. B Operasi Geometri - Operasi Ratasi
# Fachri Rahmansyah
# 1217070023 PCD TSEB

import cv2
import numpy as np
image = cv2.imread('images.jpg')
(height, width) = image.shape[0:2]
RotasiMatriks = cv2.getRotationMatrix2D((width/2, height/2),-90,0.5)
RotasiCitra = cv2.warpAffine(image, RotasiMatriks, (width, height))
cv2.imshow('Citra Rotasi', RotasiCitra)
cv2.waitKey(0)

## 6. C Operasi Geometri - Operasi Flipping
# Fachri Rahmansyah
# 1217070023 PCD TSEB

import cv2
import numpy as np
image = cv2.imread('images.jpg')
flip_hor=cv2.flip(image,1)
flip_ver=cv2.flip(image,0)
flip_verhor=cv2.flip(image,-1)
cv2.imshow('Citra', image)
cv2.imshow('Citra Flip Horizontal', flip_hor)
cv2.imshow('Citra Flip Vertical', flip_ver)
cv2.imshow('Citra Flip Vertical-Horizontal', flip_verhor)
cv2.waitKey(0)

7. penskalaan citra
# Fachri Rahmansyah
# 1217070023 PCD TSEB Program penskalaan citra
import cv2

# membaca dua gambar
image = cv2.imread('nurhadi.jpg')

zoom_factor = 1.5

height, width = image.shape[:2]

new_height = int(height * zoom_factor)
new_width = int(width * zoom_factor)

scaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

cv2.imshow('Original Image', image)
cv2.imshow('Image Zooming', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



