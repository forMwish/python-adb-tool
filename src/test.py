import cv2 as cv
import numpy as np
import sys
import os

img = cv.imread("desktop.jpg")

if img is None:
    sys.exit("read failed")

img = np.transpose(img, (1, 0, 2))
cv.imwrite("desktop.png", img)

os.system()