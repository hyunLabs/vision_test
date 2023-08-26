import cv2
import os
from PIL import Image
import imagehash
import numpy as np
# hash = imagehash.average_hash(Image.open('tests/data/imagehash.png'))
# print(hash)

def img2avgHashLib(img_src):
    hash = imagehash.average_hash(Image.open(img_src))
    return hash

def img2avgHashLib2(img_src):
    image = Image.open(img_src)
    image = image.convert('L').resize((8, 8))
    
    pixels = np.asarray(image)
    avg = np.mean(pixels)

	# create string of bits
    bin = 1 * (pixels > avg)
   
    dhash = []
    for row in bin.tolist():
        s = ''.join([str(i) for i in row])
        dhash.append('%02x'%(int(s,2)))
    dhash = ''.join(dhash)
    
    return dhash

def img2avgHash(img_src):
    img = cv2.imread(img_src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (8, 8))
    avg = gray.mean()
    bin = 1 * (gray > avg)
    
    dhash = []
    for row in bin.tolist():
        s = ''.join([str(i) for i in row])
        dhash.append('%02x'%(int(s,2)))
    dhash = ''.join(dhash)

    return dhash

def img2avgHashList(path):
    img_name_list = os.listdir(path)
    
    hash_list = []
    
    for img_name in img_name_list:
        img_src = os.path.join(path, img_name)
    
        hash_list.append(img2avgHash(img_src))
    
    return hash_list