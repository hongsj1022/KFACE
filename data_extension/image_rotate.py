import cv2
import pandas as pd
import imutils


data = pd.read_excel('10s_label.xlsx', index_col='filepath')
names = data.index

print("Complete to read excel!")

#rotate +4
for name in names :
    name = name.replace('\\','/')

    image = cv2.imread(name)
    rotate_image = imutils.rotate(image,4)
    filename = name.replace('.jpg','_rotate_p4.jpg')

    cv2.imwrite(filename, rotate_image)

print("Finish to rotate 4")

#rotate -4
for name in names :
    name = name.replace('\\','/')

    image = cv2.imread(name)
    rotate_image = imutils.rotate(image,-4)
    filename = name.replace('.jpg','_rotate_m4.jpg')

    cv2.imwrite(filename, rotate_image)

print("Finish to rotate -4")

#rotate +8
for name in names :
    name = name.replace('\\','/')

    image = cv2.imread(name)
    rotate_image = imutils.rotate(image,8)
    filename = name.replace('.jpg','_rotate_p8.jpg')

    cv2.imwrite(filename, rotate_image)

print("Finish to rotate 8")

#rotate -8
for name in names :
    name = name.replace('\\','/')

    image = cv2.imread(name)
    rotate_image = imutils.rotate(image,-8)
    filename = name.replace('.jpg','_rotate_m8.jpg')

    cv2.imwrite(filename, rotate_image)

print("Finish to rotate -8")

#rotate +12
for name in names :
    name = name.replace('\\','/')
            
    image = cv2.imread(name)
    rotate_image = imutils.rotate(image,12)
    filename = name.replace('.jpg','_rotate_p12.jpg')

    cv2.imwrite(filename, rotate_image)

print("Finish to rotate 12")

#rotate -12

for name in names :
    name = name.replace('\\','/')
    
    image = cv2.imread(name)
    rotate_image = imutils.rotate(image,-12)
    filename = name.replace('.jpg','_rotate_m12.jpg')

    cv2.imwrite(filename, rotate_image)

print("Finish to rotate -12")

#rotate +16

for name in names :
    name = name.replace('\\','/')
    
    image = cv2.imread(name)
    
    rotate_image = imutils.rotate(image,16)
    
    filename = name.replace('.jpg','_rotate_p16.jpg')
    cv2.imwrite(filename, rotate_image)

print("Finish to rotate 16")

#rotate -16
for name in names :
    name = name.replace('\\','/')
    
    image = cv2.imread(name)

    rotate_image = imutils.rotate(image,-16)
    filename = name.replace('.jpg','_rotate_m16.jpg')
    cv2.imwrite(filename, rotate_image)

print("Finish to rotate -16")
