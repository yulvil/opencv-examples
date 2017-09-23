#!/usr/bin/env python

import cv2
import numpy as np

def show_img(img):
  cv2.imshow('Output', img)
  k = cv2.waitKey(0) & 0xFF
  cv2.destroyAllWindows()

img = cv2.imread('in.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = 255*(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) > 5).astype('uint8')

blur1 = cv2.blur(gray, (1,1))
blur3 = cv2.blur(gray, (3,3))
blur5 = cv2.blur(gray, (5,5))
blur = [blur1, blur3, blur5]

medblur1 = cv2.medianBlur(gray, 1)
medblur3 = cv2.medianBlur(gray, 3)
medblur5 = cv2.medianBlur(gray, 5)
medblur = [medblur1, medblur3, medblur5]

gauss1 = cv2.GaussianBlur(gray, (1, 1), 0)
gauss3 = cv2.GaussianBlur(gray, (3, 3), 0)
gauss5 = cv2.GaussianBlur(gray, (5, 5), 0)
gauss = [gauss1, gauss3, gauss5]

bila1 = cv2.bilateralFilter(gray, 9, 50, 50)
bila3 = cv2.bilateralFilter(gray, 9, 100, 100)
bila5 = cv2.bilateralFilter(gray, 9, 150, 150)
bila = [bila1, bila3, bila5]

cv2.imwrite('filtering.jpg', np.vstack((np.hstack([gray, gray, gray]), np.hstack(blur), np.hstack(medblur), np.hstack(gauss), np.hstack(bila))))
