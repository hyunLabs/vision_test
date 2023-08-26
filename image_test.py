from frameExtract.frameExtraxtDemo import frameExtraxt
from imageHashDemo import img2avgHash, img2AvgBin, hamming_distance, cosine_simillar, jaccard_simillar

import os
import csv
import sys

def imageHash2csvExe(input, output):
    # path = r'D:\05.python\ffmpeg-5.1.2-full_build\ffmpeg-5.1.2-full_build\bin\test'
    
    img_name_list = os.listdir(input)
    
    hash_list = []
    
    csv_path = os.path.join(output, 'imageHash.csv')
    
    f = open(csv_path,'w', newline='')
    wr = csv.writer(f)
    wr.writerow(['num', 'hash', 'path', 'hamming', 'jaccard', 'cosine'])

    current_hash_bin = None

    for idx, img_name in enumerate(img_name_list):
        
        if(img_name.find('.jpg') > -1 or img_name.find('.jpeg') > -1 or img_name.find('.png') > -1):
            img_src = os.path.join(input, img_name)

            if idx == 0:
                current_hash_bin = img2AvgBin(img_src)

            next_hash_bin = img2AvgBin(img_src)
            hamming_dist = hamming_distance(current_hash_bin, next_hash_bin)
            cosine = cosine_simillar(current_hash_bin, next_hash_bin)
            jaccard = jaccard_simillar(current_hash_bin, next_hash_bin)
        
            wr.writerow([idx+1, img2avgHash(next_hash_bin), img_src, hamming_dist, jaccard, cosine])
            
            current_hash_bin = next_hash_bin
    f.close()

def frameExtraxtExe(input, output):
    # input = r'D:\05.python\ffmpeg-5.1.2-full_build\ffmpeg-5.1.2-full_build\bin\test.mp4'

    # WriteIFrame(input)
    frameExtraxt(input, output)
if __name__ == "__main__":
    # path = r'D:\05.python\ffmpeg-5.1.2-full_build\ffmpeg-5.1.2-full_build\bin\test'
    # imageHash2csvExe(path)
    # input = r'D:\05.python\ffmpeg-5.1.2-full_build\ffmpeg-5.1.2-full_build\bin\test.mp4'
    # frameExtraxtExe(input)
    # inputs = input('video input path : ')
    # output = input('frame output path : ')
    # frameExtraxtExe(inputs, output)

    inputs = input('img_dir input path : ')
    output = input('csv output path : ')
    imageHash2csvExe(inputs, output)