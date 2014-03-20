# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 14:33:28 2014

@author: ralph
"""

# This script lets you detect faces from an image, crop them and save the cropped images in extra files

import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')			# define cascade classifier


img = cv2.imread('test.jpg') 													# define test image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #im = Image.open('test.jpg')
    crop_img = img[y:y+h, x:x+h]
    cv2.imwrite('cropped(%d).jpg' % x, crop_img)
    #cv2.imshow("cropped", crop_img)
    #img.crop((x,y,x+w,y+h)).save('cropped(%d).jpg' % x)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

