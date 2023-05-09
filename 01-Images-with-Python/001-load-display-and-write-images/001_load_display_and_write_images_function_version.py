import argparse
import cv2


def get_image() -> cv2:
    """
    Load the image with argument parser

    Parameters
    ----------
    No parameters


    Returns
    -------
    cv2
        an image object from given path
    """

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the image to load")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])
    return image


def display_info(image) -> None:
    """
    Method to display the image width, height, and the number of channels
    We are assuming the image is a Numpy array

    Parameters
    ----------
    image : cv2
        The image object (Numpy's array)


    Returns
    -------
    None
    """

    print(f"Width of the image: {image.shape[1]} pixels")
    print(f"Height of the image: {image.shape[0]} pixels")
    print(f"Number of channels: {image.shape[2]}")


def show_image(image, duration=500) -> None:
    """
    Method to show the image and wait given time or for a keypress

    Parameters
    ----------
    image : cv2
        The image object (Numpy's array)
    duration : int
        Time in miliseconds


    Returns
    -------
    None
    """

    cv2.imshow("Image", image)
    cv2.waitKey(duration)


def save_image(image, new_name) -> None:
    """
    Method to save the image under the given name

    Parameters
    ----------
    image : cv2
        The image object (Numpy's array)
    new_name : str
        New name of the written image


    Returns
    -------
    None
    """

    cv2.imwrite(f"{new_name}.jpg", image)


if __name__ == '__main__':
    # read an image
    my_image = get_image()

    # display information about the image
    display_info(my_image)

    # show the image
    show_image(my_image, duration=2000)

    # create a copy of the image
    save_image(my_image, new_name="copy_of_my_image_function_version")
