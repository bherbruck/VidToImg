import os
import time
import cv2

def capture_images(vidfile, interval=0):
    """Read a video file and convert to images
    
    Args:
        vidfile (str): video file to read
        interval (float, optional): how often to capture an image from the video in seconds. Defaults to 1.0.
    """
    vidcap = cv2.VideoCapture(vidfile)
    success, image = vidcap.read()
    print(success)
    if success:
        vidname = os.path.splitext(os.path.basename(vidfile))[0]
        vidpath = os.path.dirname(vidfile)
        imgpath = "{}/{}_images".format(vidpath, vidname)
        print("Found video at: ".format(vidpath))
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
            time.sleep(interval)
    else:
        print("Something went wrong... check your file path/name")