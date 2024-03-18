# -*- coding: utf-8 -*-

"""
Program that takes an image of Bradski & Kaebler's Learning OpenCV
book and performs 4 types of blurring on it, as well as shows you the file
size of each'
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

def get_file_size(filename):
    return os.path.getsize(filename)

def avg_blur(img):
    kernel = np.ones((5,5),np.float32)/25
    avg = cv2.filter2D(img,-1,kernel)
    cv2.imwrite("images/avg.jpg", avg)
    return avg
    
def gaussian_blur(img):
    sigma = 1.0
    ksize = 5
    gaussian = cv2.GaussianBlur(img, (ksize, ksize), sigma)
    cv2.imwrite("images/gaussian.jpg", gaussian)
    return gaussian
    
def median_blur(img):
    median = cv2.medianBlur(img,5)
    cv2.imwrite("images/median.jpg", median)
    return median
    
def bilateral_blur(img):
    bilateral = cv2.bilateralFilter(img,9,75,75)
    cv2.imwrite("images/bilateral.jpg", bilateral)
    return bilateral
    
    

img = cv2.imread(r"images/book.jpg")
plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.text(0, -60, f"Size: {get_file_size('images/book.jpg')} bytes", color='black')

# apply and plot different blur algorithms
res_avg = avg_blur(img)
plt.subplot(232),plt.imshow(res_avg),plt.title('Average')
plt.xticks([]), plt.yticks([])
plt.text(0, -60, f"Size: {get_file_size('images/avg.jpg')} bytes", color='black')


res_gaussian = gaussian_blur(img)
plt.subplot(233),plt.imshow(res_gaussian),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.text(0, -60, f"Size: {get_file_size('images/gaussian.jpg')} bytes", color='black')

res_median = median_blur(img)
plt.subplot(234),plt.imshow(res_median),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.text(0, -60, f"Size: {get_file_size('images/median.jpg')} bytes", color='black')


res_bilateral = bilateral_blur(img)
plt.subplot(235),plt.imshow(res_bilateral),plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.text(0, -60, f"Size: {get_file_size('images/bilateral.jpg')} bytes", color='black')

plt.show()