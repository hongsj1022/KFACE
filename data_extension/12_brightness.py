import cv2
import numpy as np
import pandas as pd

#make excel file previously to read path of images
data = pd.read_excel('/home/super/KFACE/10s_label.xlsx', index_col='filepath')
names = data.index
print("Complete to read excel!")

imgNum = 1

for name in names:
    name = name.replace('\\','/')

    image = cv2.imread(name)
    A = np.ones(image.shape, dtype="uint8") * 11
    B = np.ones(image.shape, dtype="uint8") * 22
    C = np.ones(image.shape, dtype="uint8") * 33
    D = np.ones(image.shape, dtype="uint8") * 44
    E = np.ones(image.shape, dtype="uint8") * 55
    F = np.ones(image.shape, dtype="uint8") * 66
    added_A = cv2.add(image, A)
    subtracted_A = cv2.subtract(image, A)
    added_B = cv2.add(image, B)
    subtracted_B = cv2.subtract(image, B)
    added_C = cv2.add(image, C)
    subtracted_C = cv2.subtract(image, C)
    added_D = cv2.add(image, D)
    subtracted_D = cv2.subtract(image, D)
    added_E = cv2.add(image, E)
    subtracted_E = cv2.subtract(image, E)
    added_F = cv2.add(image, F)
    subtracted_F = cv2.subtract(image, F)
        
    
    filename_add_A = name.replace('.jpg','_L11.jpg')
    filename_subtract_A = name.replace('.jpg','_D11.jpg')
    filename_add_B = name.replace('.jpg','_L22.jpg')
    filename_subtract_B = name.replace('.jpg','_D22.jpg')
    filename_add_C = name.replace('.jpg','_L33.jpg')
    filename_subtract_C = name.replace('.jpg','_D33.jpg')
    filename_add_D = name.replace('.jpg','_L44.jpg')
    filename_subtract_D = name.replace('.jpg','_D44.jpg')
    filename_add_E = name.replace('.jpg','_L55.jpg')
    filename_subtract_E = name.replace('.jpg','_D55.jpg')
    filename_add_F = name.replace('.jpg','_L66.jpg')
    filename_subtract_F = name.replace('.jpg','_D66.jpg')

    cv2.imwrite(filename_add_A, added_A)
    cv2.imwrite(filename_subtract_A, subtracted_A)
    cv2.imwrite(filename_add_B, added_B)
    cv2.imwrite(filename_subtract_B, subtracted_B)
    cv2.imwrite(filename_add_C, added_C)
    cv2.imwrite(filename_subtract_C, subtracted_C)
    cv2.imwrite(filename_add_D, added_D)
    cv2.imwrite(filename_subtract_D, subtracted_D)
    cv2.imwrite(filename_add_E, added_E)
    cv2.imwrite(filename_subtract_E, subtracted_E)
    cv2.imwrite(filename_add_F, added_F)
    cv2.imwrite(filename_subtract_F, subtracted_F)

    print(imgNum, "images have extended!")
    imgNum+=1

