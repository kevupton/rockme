# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:47:33 2015

@author: Gavin
"""

import DGS
import timeit
import numpy as np
import time
import cv2
import matplotlib as mpl
from matplotlib import pyplot


def process(image_file):
    density = 1 # process every 10 lines
    res = 1.3 # mm/pixel
    doplot = 0 # don't make plots
    #image_folder = 'C:/Users/Gavin/Downloads/'
    #DGS.dgs(image_folder,density,doplot,res)
    #image_file = 'C:/Users/Gavin/Downloads/Apache-Brown-sml.jpg'
    mnsz, srt, sk, kurt, pd, xi, yi = DGS.dgs(image_file,density,doplot,res)
    return mnsz, srt, sk, kurt, pd, xi, yi

#print(timeit.timeit("process()", setup="from __main__ import process", number = 10))


start_time = time.time()
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 0

camera = cv2.VideoCapture(camera_port)

def get_image():
 retval, im = camera.read()
 return im

filePath = "test.png"
count = 0
cap = cv2.VideoCapture(0)
#124.768
time_taken = time.time()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if (time.time() - time_taken >= 3):
        count += 1
        camera_capture = get_image()
        cv2.imwrite(filePath, camera_capture)
        time_taken = time.time()
        density = 1 # process every 10 lines
        res = 1.3 # mm/pixel
        doplot = 1 # don't make plots
        mnsz, srt, sk, kurt, pd, xi, yi = DGS.dgs(filePath,density,doplot,res)
        pyplot.plot(xi,yi)
        pyplot.show()
        #mnsz, srt, sk, kurt, pd = process(filePath)
        print pd
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

 
del(camera)