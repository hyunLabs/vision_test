import cv2
import os

def hamming_distance(a, b):
    a = a.reshape(1, -1)[0]
    b = b.reshape(1, -1)[0]
    
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    
    return count / len(a)

# 교집합 / 합집합
def jaccard_simillar(a, b):
    
    a = img2avgHash(a)
    b = img2avgHash(b)
    
    a = set(list(str(a)))
    b = set(list(str(b)))
    
    return float(len(a.intersection(b)) / len(a.union(b)))

# 두 벡터 크기의 곱 / 두 벡터의 내적
def cosine_simillar(a, b):
    a = a.reshape(1, -1)[0]
    b = b.reshape(1, -1)[0]
    
    a_sum = 0
    b_sum = 0
    
    c_sum = 0
    
    for i in range(len(a)):
        a_sum += a[i]**2
        b_sum += b[i]**2
        
        c_sum += a[i] * b[i]
    
    return c_sum / ((a_sum * b_sum)**(1/2))

def img2AvgBin(img_src):

    img = cv2.imread(img_src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (8, 8))
    avg = gray.mean()
    bin = 1 * (gray > avg)
    
    return bin


def img2avgHash(bin):

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