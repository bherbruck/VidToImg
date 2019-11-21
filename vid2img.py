import os
import cv2


def capture_images(video_file, image_quantity=None, scale=1.00, square=False, output_dir=None):
    """
    Read a video file and convert to images
    
    Args:
        vidfile (str): Video file and path to read.
        image_quantity (int, optional): Quantity of images to capture, divides frames equally. Defaults to None.
        scale (float, optional): Scaling factor to apply to the image. Defaults to 1.00.
        square (bool, optional): Todo. Defaults to False.
        output_dir (str): Todo. Defaults to None.
    """
    video_capture = cv2.VideoCapture(video_file)
    success, image = video_capture.read()
    dimensions = image.shape
    if success:
        # Set up file paths
        video_name = os.path.splitext(os.path.basename(video_file))[0]
        video_dir = os.path.dirname(video_file)
        print("Found video at: {}".format(video_dir))

        # Get number of frames in the video
        frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

        # Handle 0 or None values for image_quantity
        if image_quantity is None or image_quantity == 0 or image_quantity > frame_count:
            image_quantity = frame_count

        # Divide frames evenly to capture
        frame_interval = int(frame_count / image_quantity)
        count = 0
        frame = 0

        # Create directory for saving images
        if output_dir is None:
            image_dir = "{}/{}_images".format(video_dir, video_name)
        else:
            image_dir = output_dir
        if not os.path.exists(image_dir):
            os.mkdir(image_dir)
            print("Creating directory: {}".format(image_dir))

        # Loop through images in video_capture
        while success:
            success, image = video_capture.read()
            # Check if current frame is divisible by frame_interval
            if success and not image_quantity is None and (frame + 1) % frame_interval == 0:
                image_file = "{}/{}_{}.jpg".format(image_dir, video_name, count)
                resized_image = cv2.resize(image, None, fx=scale, fy=scale)
                # Make the image square
                if square:
                    image_height, image_width, _ = resized_image.shape
                    cropped_start = int((image_width / 2) - (image_height / 2))
                    c = [0,image_height, cropped_start,image_height]
                    resized_image = resized_image[0:image_height, cropped_start:image_height+cropped_start]
                # Save the image
                cv2.imwrite(image_file, resized_image)
                print("\rCreating image file: {}".format(image_file), end="")
                count += 1
            frame += 1
        print("\n{} images created in {}".format(count, image_dir))
    else:
        print("Something went wrong... check your file path/name")
