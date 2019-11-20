import cv2
import os
from PIL import Image

PATH = './Raw_Dataset'

file_names = []

for root, folder, files in os.walk(PATH):
    for f in files:
        im = cv2.imread(os.path.join(root, f))
        x, y, c = im.shape
        if x < 224 or y < 224 or x < 224 and y < 224:
            os.remove(os.path.join(root,f))


        
print("Removed Files.")




