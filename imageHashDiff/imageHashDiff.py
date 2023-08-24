import sys
import os
import numpy 
import cv2
import matplotlib.pyplot as plt

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from imageHash.imageHashDemo import img2avgHashLib, img2avgHash

threshold = 0.9

def img2hashBin(img_src):
    img = cv2.imread(img_src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (16, 16))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi

def hamming_distance(a, b):
    a = a.reshape(1,-1)
    b = b.reshape(1,-1)
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a !=b).sum()
    return distance

img_path = input('input path: ')
output = input('output path: ')

hash_diff_list = []

hash = img2hashBin(os.path.join(img_path, os.listdir(img_path)[0]))

for img_name in os.listdir(img_path):
    img_src = os.path.join(img_path, img_name)

    otherhash = img2hashBin(img_src)
    
    diff = hamming_distance(hash, otherhash)
    if diff > threshold:
        hash_diff_list.append(diff)
        
print(hash_diff_list)