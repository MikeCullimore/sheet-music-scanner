"""
todo:
Binarise image first for simplicity.
Run length encoding on image cols.
    Rotate image 90 degrees then use cv2.createRLEImage? (Faster scanning rows given memory layout?)
Plot histogram of black pixel run length: is median 
Optimise:
    Profile.
    Use every nth column of image to calculate stave line thickness rather than all.
    Throw away runs not within +/- tolerance of median.
    Join them up as cubic splines (avoid need for connected components, filtering out other features).
"""

import os.path

from cv2 import (
    imread,
    threshold,
    THRESH_BINARY,
    THRESH_OTSU
)
import matplotlib.pyplot as plt
import numpy as np

folder = 'images'

def main():
    filename = 'Lo How a Rose GIMP binary.png'
    # filename = 'Lo How a Rose GIMP.jpg' # todo: still RGB? Convert to greyscale!
    image = _imread(filename)
    # image, _ = threshold(image, 0, 255, THRESH_BINARY+THRESH_OTSU)

    # find_staff_lines(image)
    
    # array = [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    column = 300
    array = image[:, column, 0]
    debug_rle(array)

def debug_rle(array):
    # todo: plot run length histogram.
    runs = run_length_encode(array)
    print(runs)
    run_lengths = np.array([run[1] for run in runs if run[0] == 0])

    line_thickness = np.median(run_lengths)
    print(f'Estimated stave line thickness: {line_thickness}')

    plt.figure()
    plt.hist(run_lengths, bins=50)
    plt.show()

def run_length_encode(array):
    runs = []
    length = 1
    previous = array[0]
    for index, value in enumerate(array[1:]):
        if value == previous:
            length += 1
        else:
            runs.append([previous, length, index])
            length = 1
            previous = value
    runs.append([value, length, index])
    return runs

def find_staff_lines(image):
    # plt.figure()
    # plt.imshow(image, cmap='gray')
    # plt.xticks([])
    # plt.yticks([])
    # plt.show()

    height, width, _ = image.shape
    print(width, height)

    column = width//2 + 50 # choose a column that intersects the stave lines.
    image_column = image[:, column, :]

    # todo: binarise the image first.
    # todo: interaction (slider to move column).
    axs = plt.figure().subplots(1, 2)
    axs[0].imshow(image)
    axs[0].axvline(column, color='r')
    axs[0].set_xticks([])
    axs[0].set_yticks([])
    axs[0].set_title('Image with selected column')
    axs[1].plot(image_column) # todo: plot as horizontal projection: how?
    axs[1].set_xticks([])
    axs[1].set_yticks([])
    axs[1].set_title('Pixel values in that column')
    plt.show()

def _imread(filename):
    return imread(get_filepath(filename))

def get_filepath(filename):
    return os.path.join(folder, filename)

if __name__ == '__main__':
    main()
