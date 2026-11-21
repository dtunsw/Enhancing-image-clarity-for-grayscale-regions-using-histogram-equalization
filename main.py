import cv2
import matplotlib.pyplot as plt
import numpy as np

#READ IMAGE
img = cv2.imread("example.png")
if img is None:
    print ("no image exist!")
    exit()
