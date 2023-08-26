import ffmpegio
import cv2
import os

def checkDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def frameExtraxt2(input, output=None, ss='00:00:00', t='00:03:00', frame_type='I'):
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

def frameExtraxt(input, output=None, ss='00:00:00', t='00:03:00', frame_type='I'):

    path = os.path.split(input)[0]
    file_name = os.path.splitext(os.path.split(input)[1])[0]
    
    if output == None or output == '':
        
        path = os.path.join(path, file_name)
        
        checkDir(path)
        
        img_path = os.path.join(path, file_name)
        output = os.path.join(img_path, '%4d.jpg')
    else:
        path = os.path.join(output, file_name)
        
        checkDir(path)

        output = os.path.join(path, '%4d.jpg')
    
    option_dict = {"ss": ss, "t": t, "vf": "select=eq(pict_type\," + frame_type + ")", "vsync": "2"}

    ffmpegio.transcode(input, output, **option_dict)
