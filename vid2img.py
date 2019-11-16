import os
import cv2

def capture_images(vidfile, qtyframes=None):
    """
    Read a video file and convert to images

    Args:
        vidfile (str): Video file and path to read
        frames (int, optional): If not None, divide the video into specified number of images Defaults to None.
    """
    vidcap = cv2.VideoCapture(vidfile)
    success, image = vidcap.read()
    if success:
        # Set up file paths
        vidname = os.path.splitext(os.path.basename(vidfile))[0]
        vidpath = os.path.dirname(vidfile)
        imgpath = "{}/{}_images".format(vidpath, vidname)
        print("Found video at: {}".format(vidpath))

        # Get number of frames in the video
        framecount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Handle 0 or None values for frames
        if qtyframes is None or qtyframes == 0:
            qtyframes = framecount

        # Divide frames evenly to capture
        frameinterval = int(framecount / qtyframes)
        count = 0
        frame = 0

        # Create directory for images 
        if not os.path.exists(imgpath):
            os.mkdir(imgpath)
            print("Creating directory: {}".format(imgpath))

        # Loop through images in video capture
        while success:
            success, image = vidcap.read()
            # Check if current frame is divisible by frame interval
            if not qtyframes is None and (frame + 1) % frameinterval == 0:
                imgfile = "{}/{}_{}.jpg".format(imgpath, vidname, count)
                cv2.imwrite(imgfile, image)
                print("\rCreating image file: {}".format(imgfile), end="")
                count += 1
            frame += 1
        print("\n{} images created in {}".format(qtyframes, imgpath))
    else:
        print("Something went wrong... check your file path/name")


