# -*- coding: utf-8 -*-
"""
Performs simple sobel and then canny edge detection on an image of the MiRo robot
developed by consequential robotics
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

def first_order(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  smooth_gray = cv2.GaussianBlur(gray,(3,3), 0, 0) 
  
  sobelx = cv2.Sobel(src=smooth_gray, ddepth=cv2.CV_32F, dx=1, dy=0) # Sobel Edge Detection on the X axis
  sobely = cv2.Sobel(src=smooth_gray, ddepth=cv2.CV_32F, dx=0, dy=1)
  magnitude = cv2.magnitude(sobelx, sobely)
  ret,th1 = cv2.threshold(magnitude, 100, 255, cv2.THRESH_BINARY)
  return th1

def canny(img):
    canny_edge = cv2.Canny(img,100,200)
    return canny_edge

img = cv2.imread(r"images/miro.jpg") #source from https://static.rapidonline.com/catalogueimages/product/70/92/s70-9200p01wl.jpg
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(131),plt.imshow(rgb_img),plt.title('Original')
plt.xticks([]), plt.yticks([])

sobel = first_order(img)
rgb_sobel = cv2.cvtColor(sobel, cv2.COLOR_BGR2RGB)
plt.subplot(132),plt.imshow(rgb_sobel),plt.title('Sobel')
plt.xticks([]), plt.yticks([])

canny_edge = canny(img)
rgb_canny = cv2.cvtColor(canny_edge, cv2.COLOR_BGR2RGB)
plt.subplot(133),plt.imshow(rgb_canny),plt.title('Canny')
plt.xticks([]), plt.yticks([])