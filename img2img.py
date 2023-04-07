import time
import numpy as np
import Tools.utils as utils
import Tools.converter as converter
import cv2

img = utils.textImg_generator() # Generate a random image
# img = cv2.imread('Data/data1.jpg', 1)  # Read an image
# img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

stat_time = time.time()
ascii_art = converter.image_to_ascii(img, width=img.shape[1])
print(int((time.time() - stat_time) * 1000), 'ms')

show_img = np.hstack((img, ascii_art))
cv2.imshow('random_image.jpg', show_img)
# cv2.imwrite('Result/random_image_{}.jpg'.format(int(stat_time)), show_img)
cv2.waitKey(0)
