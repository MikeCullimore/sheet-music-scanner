"""
main.py

todo:
Analyse 'Lo How a Rose GIMP.jpg'
    Stave line straightness
    Bar line verticality.
    Orthogonality?
    Note head size.
    Stave line spacing.
Replace desaturate with method like GIMP > Colours > Desaturate > Colour to Grey.
Optimise contrast (like GIMP via Levels).
OpenCV rather than Pillow?
Type annotations.
"""

import os.path

from PIL import Image, ImageFilter

folder = 'images'

def main():
    detect_edges()
    # convert_greyscale_example()

def detect_edges():
    filename = 'Lo How a Rose GIMP.jpg'
    image = imread(filename)
    edges = image.filter(ImageFilter.FIND_EDGES)
    imsave(edges, 'tmp.png')

def convert_greyscale_example():
    input_filename = 'Lo How a Rose.jpg'
    root, ext = os.path.splitext(input_filename)
    output_filename = root + ' edited' + ext
    input_image = imread(input_filename)
    output_image = desaturate(input_image)
    imsave(output_image, output_filename)

def desaturate(image):
    return image.convert('L')

def imread(filename):
    return Image.open(get_filepath(filename))

def imsave(image, filename):
    image.save(get_filepath(filename), quality=95)

def get_filepath(filename):
    return os.path.join(folder, filename)

if __name__ == '__main__':
    main()
