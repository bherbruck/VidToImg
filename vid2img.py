from os import path, mkdir
from time import sleep
from cv2 import VideoCapture, imwrite

def capture_images(vidfile, interval=1.0):
    """Read a video file and convert to images
    
    Args:
        vidfile (str): video file to read
        interval (float, optional): how often to capture an image from the video in seconds. Defaults to 1.0.
    """
    vidcap = VideoCapture(vidfile)
    success, image = vidcap.read()
    print(success)
    if success:
        vidname = path.splitext(path.basename(vidfile))[0]
        vidpath = path.dirname(vidfile)
        imgpath = "{}/{}_images".format(vidpath, vidname)
        print("Found video at: ".format(vidpath))
        count = 0
        if not path.exists(imgpath):
            mkdir(imgpath)
            print("Creating directory: {}".format(imgpath))
        while success:
            success, image = vidcap.read()
            imgfile = "{}/{}_{}.jpg".format(imgpath, count, vidname)
            imwrite(imgfile, image)
            print("Creating image file: {}".format(imgfile))
            count += 1
            sleep(interval)
    else:
        print("Something went wrong... check your file path/name")
            

capture_images("/home/brenn/Videos/eggvid.mp4")