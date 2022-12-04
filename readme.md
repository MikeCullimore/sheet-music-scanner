# sheet-music-scanner

Goals: given photo of sheet music:
* Desaturate
* Improve contrast
* Correct for image distortion
* Parse the pitches and their durations

## Activating the virtual environment

Linux: at bash prompt, from root directory:
```
source venv/bin/activate
```

### Installing dependencies

(After activating the virtual environment)
```
pip install -r requirements.txt
```

## Useful links

[Optical Music Recognition on Wikipedia](https://en.wikipedia.org/wiki/Optical_music_recognition)

## Ideas for correcting image distortion

* Similar to galvo calibration (2d coordinate transformation, smooth polynomials).
* Try to work out surface normal at each point in image, then straighten them all.
    * Start with coarse grid then subdivide each cell into four cells.
    * Constraints: cell corners must move together (piecewise continuous).
    * If page curving away, features will appear smaller, can correct for that consistently.
* What metrics to use for quality of output?
    * Straightness
    * Orthogonality
    * Uniformity of magnification: note head sizes? Distance between stave lines?
* Define a transformation matrix then tweak the parameters manually and try to obtain a corrected image (if unable to, is transformation itself not general enough?).