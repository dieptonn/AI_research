import cv2

img = cv2.imread(
    'D:\Code\Python\pythonTutorial\R10_PBL\AI_reasearch\imgProcessing_opencv\game.png', -1)

# # img = cv2.resize(img, (300, 300))  # width=300, height=300
# img = cv2.resize(img, (0, 0), fx=0.6, fy=0.6)

# cv2.imshow('game', img)
# k = cv2.waitKey()

# print(k)
# print(ord('s'))

# if (k == ord('s')):
#     cv2.imwrite(
#         'D:\Code\Python\pythonTutorial\R10_PBL\AI_reasearch\imgProcessing_opencv\game2.png', img)


img = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow('game', img)
k = cv2.waitKey()
