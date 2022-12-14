from cv2 import (
    BORDER_REPLICATE,
    imread,
    INTER_CUBIC,
    projectPoints,
    remap
)
import matplotlib.pyplot as plt
import numpy as np

REMAP_DECIMATE = 16  # Downscaling factor for remapping image

def main():
    filename = 'images/Lo How a Rose GIMP.jpg'
    image = imread(filename)
    
    plt.imshow(image)
    plt.show()

    alpha = 0
    beta = 0
    rvec = None # todo
    tvec = None # todo

def project_xy(xy_coords, alpha, beta, rvec, tvec):
    poly = np.array([alpha + beta, -2 * alpha - beta, alpha, 0])
    xy_coords = xy_coords.reshape((-1, 2))
    z_coords = np.polyval(poly, xy_coords[:, 0])
    objpoints = np.hstack((xy_coords, z_coords.reshape((-1, 1))))
    cameraMatrix = None # todo
    distortionCoefficients = np.zeros(5) # todo: explore non-zero.
    image_points, _ = projectPoints(
        objpoints,
        rvec,
        tvec,
        cameraMatrix,
        distortionCoefficients
    )
    return image_points

def remap_image(image, image_x_coords, image_y_coords):
    return remap(
        image,
        image_x_coords,
        image_y_coords,
        INTER_CUBIC,
        None,
        BORDER_REPLICATE,
    )

if __name__ == '__main__':
    main()
