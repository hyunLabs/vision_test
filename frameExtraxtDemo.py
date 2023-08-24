import ffmpegio
import cv2
import os

def checkDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def WriteIFrame(input, output=None, ss='00:00:00', t='00:03:00', frame_type='I'):
    """_summary_

    Returns:
        _type_: int
        _doc_: I-Frame 개수
    """
    path = os.path.split(input)[0]
    file_name = os.path.splitext(os.path.split(input)[1])[0]
    
    img_path = os.path.join(path, file_name)

    checkDir(img_path)

    rates, data = ffmpegio.media.read(input, ss=ss, t=t, vf='select=eq(pict_type\,' + frame_type + ')', vsync='2')

    keyFrames = data['v:0']

    for index, frame in enumerate(keyFrames):
        img_src = str(index + 1).zfill(5) + '.jpg'
        
        img_src = os.path.join(img_path, img_src)
        
        ffmpegio.image.write(img_src, frame, overwrite=True)
        
    return len(keyFrames[0])

# input = r'D:\05.python\ffmpeg-5.1.2-full_build\ffmpeg-5.1.2-full_build\bin\test.mp4'

# WriteIFrame(input, t='00:00:10', frame_type='B')