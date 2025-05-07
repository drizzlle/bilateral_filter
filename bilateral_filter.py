import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt


def BilateralFilter():

    root_dir = os.getcwd()
    PhotoPath = os.path.join(root_dir, "bilateral_filter/data", "my_tesla.jpeg")
    # Read the image
    image = cv.imread(PhotoPath)
    # Convert the image to RGB
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    # Apply bilateral filter
    height,width,_ = image_rgb.shape
    scale = 1/4
    width = int(width*scale)
    height = int(height*scale)
    image_rgb = cv.resize(image_rgb, (width,height))

    filtered_image = cv.bilateralFilter(image_rgb, 9,75,75)
    # Display the original and filtered images

    plt.figure()
    plt.subplot(121)
    plt.imshow(image_rgb)
    plt.subplot(122)
    plt.imshow(filtered_image)
    plt.show()
    # Save the filtered image
    output_path = os.path.join(root_dir, "results", "filtered_image.jpg")
    cv.imwrite(output_path, filtered_image)
    print(f"Filtered image saved to {output_path}")
if __name__ == "__main__":
    BilateralFilter()
    