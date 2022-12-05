"""
main.py

todo:
Replace desaturate with method like GIMP > Colours > Desaturate > Colour to Grey.
Optimise contrast (like GIMP manual)
"""

import os.path

from PIL import Image

folder = 'images'

def main():
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
