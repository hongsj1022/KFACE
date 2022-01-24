import cv2
import pandas as pd

#make excel file previously to read path of images
data = pd.read_excel('10s_label.xlsx', index_col='filepath')
names = data.index

change = 0

for name in names :
    name = name.replace('\\','/')

    image = cv2.imread(name)
    flip_image = cv2.flip(image,1)
    filename = name.replace('.jpg','_flip.jpg')

    #save image in same directory with original image
    cv2.imwrite(filename, flip_image)

    change = change + 1
    print(change, " images have flipped")


