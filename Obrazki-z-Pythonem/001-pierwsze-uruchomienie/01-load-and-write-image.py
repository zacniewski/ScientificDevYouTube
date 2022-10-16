# import the necessary packages
import argparse
import cv2


def get_image():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the image to load")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])
    return image

def display_info(image):
    # display the image width, height, and the number of channels 
    (height, width, channels) = image.shape[:3]
    print(f"Width of the image: {width} pixels")
    print(f"Height of the image: {height} pixels")
    print(f"Number of channels: {channels}")
    print(f"Type of image object: {type(image)}")

def show_image(image, time=500):
    # show the image and wait given time or for a keypress
    cv2.imshow("Image", image)
    cv2.waitKey(time)

def save_image(image):
    # save the image
    cv2.imwrite("my_new_image.jpg", image)

if __name__ == '__main__':
    my_image = get_image()
    display_info(my_image)
    show_image(my_image)
    save_image(my_image)
