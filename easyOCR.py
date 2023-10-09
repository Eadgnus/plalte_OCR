import easyocr
import numpy as np
import matplotlib.pyplot as plt
import cv2

img_ori = cv2.imread('plate.jpg')

height, width, channel = img_ori.shape

print(img_ori.shape)

plt.figure(figsize=(12, 10))
plt.imshow(img_ori, cmap='gray')