import pyautogui
# import cv2

#  Accessing Required Package and class

import datetime
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function -----   Rectifying error

# Matching the detail with suitable pattern

def error_clearance(value):
    for i in range(0,len(value)):
        v=value[i]
        # print(value[i])
        if(v.isalpha() or v.isdigit()):
            continue
        elif(v=='^' or v=='=' or v=='_' or v=='~'):
            value[i]='-'

# class Vehicle_Details:

# imoprt image for Processing text after extraction of the features

img=Image.open("C:/Users/lazmin/PycharmProjects/carplate3.jfif")

cur_time=datetime.datetime.now()

# Trying to extract all possible string from the image

output=pytesseract.image_to_string(img)

# splitting string for comparison and manipulation purpose:

Labels=list(i for i in output)

error_clearance(Labels)

# Display details



print('Car Details')
print('Number Plate : ',end='')
for i in Labels:
    if (i.isalpha() or i.isnumeric() or i=='-' or i==' '):
        print(i,end='')
print('\nEntry Date   : ',cur_time.day,'-',cur_time.month,'-',cur_time.year,sep='')

print('Entry Time   : ',cur_time.hour,':',cur_time.minute,sep='')

print('Payment      : 1.Cash     2.Via-Online')

