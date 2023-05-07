import argparse
from dataclasses import dataclass

import cv2


@dataclass
class ImageInformation:
    """
    Class to store basic image information
    """

    width: int
    height: int
    number_of_channels: int

    @staticmethod
    def get_image() -> cv2:
        """
        Load the image with argument parser

        Parameters
        ----------
        None


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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
    my_image = ImageInformation.get_image()

    # get its size and number of channels
    my_image_properties = my_image.shape

    # create new object of Image2D class
    my_image_object = ImageInformation(
        width=my_image_properties[1],
        height=my_image_properties[0],
        number_of_channels=my_image_properties[2]
    )

    # display information about the image
    ImageInformation.display_info(my_image)

    # show the image
    ImageInformation.show_image(my_image, duration=2000)

    # create a copy of the image
    ImageInformation.save_image(my_image, new_name="copy_of_my_image_class_version")
