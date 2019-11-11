import os
import cv2

def capture_images(vidfile, interval=100):
    vidcap = cv2.VideoCapture(vidfile)
    success, image = vidcap.read()
    if success:
        vidname = os.path.splitext(os.path.basename(vidfile))[0]
        vidpath = os.path.dirname(vidfile)
        imgpath = "{}/{}_images".format(vidpath, vidname)
        count = 0
        if not os.path.exists(imgpath):
            os.mkdir(imgpath)
            print("Creating directory: {}".format(imgpath))
        while success:
            success, image = vidcap.read()
            imgfile = "{}/{}_{}.jpg".format(imgpath, count, vidname)
            cv2.imwrite(imgfile, image)
            print("Creating image file: {}".format(imgfile))
            count += 1

