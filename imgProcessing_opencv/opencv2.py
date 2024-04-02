import cv2
import random

img = cv2.imread('game.png', 1)

# print(img)
print(type(img))
print(img.shape)
# print(img[511])

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(
#             0, 255), random.randint(0, 255)]


vungchon = img[0:200, 280:380]
img[50:250, 380:480] = vungchon

cv2.imshow('anh.png', img)
cv2.waitKey()
