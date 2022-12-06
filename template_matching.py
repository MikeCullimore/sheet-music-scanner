"""
Template matching example from scikit-image docs:
https://scikit-image.org/docs/stable/user_guide/getting_started.html

Trying to use template of empty stave lines to identify image features like
stave position, number of staves, page curvature.
"""

import os.path

import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.feature import match_template

def main():
    image = imread('Lo How a Rose GIMP.jpg')
    template = imread('stave lines.jpg')

    result = match_template(image, template)
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]

    fig = plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 2)
    ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('template')

    ax2.imshow(image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    hcoin, wcoin = template.shape
    rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
    ax2.add_patch(rect)

    ax3.imshow(result)
    ax3.set_axis_off()
    ax3.set_title('`match_template`\nresult')
    # highlight matched region
    ax3.autoscale(False)
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

    plt.show()

def imread(filename):
    return io.imread(os.path.join('images', filename))

if __name__ == '__main__':
    main()
