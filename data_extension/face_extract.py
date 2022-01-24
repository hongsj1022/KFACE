import cv2
import face_recognition
from face_recognition import face_locations
import pandas as pd

#make excel file previously to read path of images
data = pd.read_excel('/home/super/KFACE/KFACE/kface/10s/10s_label.xlsx',index_col='filepath')

names = data.index

imgNum = 1

for name in names :
    name = name.replace('\\','/')
    image = face_recognition.load_image_file(name)
    locs = face_locations(image, number_of_times_to_upsample = 1)
    locs = pd.DataFrame(locs,columns = ['top', 'right', 'bottom', 'left'])

    img = cv2.imread(name)

    for row in locs.iterrows():
        top,right,bottom,left = row[1][:4].astype(int)

        cropped = img[top:bottom, left:right]
        #save image
        #path can be different
        cv2.imwrite("/home/super/KFACE/KFACE/kface/10s/cropped/10s_" + str(imgNum) + ".jpg", cropped)
        print(imgNum)
        imgNum += 1
