from os import path
from time import sleep
from cv2 import VideoCapture, imwrite

def capture_images(vidfile, interval=1.0):
    """Read a video file and convert to images
    
    Args:
        vidfile (str): video file to read
        interval (float, optional): how often to capture an image from the video in seconds. Defaults to 1.0.
    """
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
            sleep(interval)
            

