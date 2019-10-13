# AugPy
A Python based Augmented Reality library

Based on the initial repo by [Juan Gallostra](https://github.com/juangallostra/augmented-reality).

## Talk at PyCon India 2019

The below link is for an introductory talk I've given on this at PyCon India, 2019. 

[Link to slides](https://docs.google.com/presentation/d/1nwUh1XZpSFy3vhp3yi5-KoIfkFSB_RJEj-2ffcVXDMk)

## Main Requirements

* Python 3.x
* OpenCV 4.x
* numpy

## Usage

* Place the image of the surface to be tracked inside the `reference` folder.
* On line 36 of `src/ar_main.py` replace `'model.jpg'` with the name of the image you just copied inside the `reference` folder.
* On line 40 of `src/ar_main.py` replace `'fox.obj'` with the name of the model you want to render. To change the size of the rendered model change the scale parameter (number `3`) in line 103 of `src/ar_main.py` by a suitable number. This might require some trial and error.
* Open a terminal session inside the project folder and run `python src/ar_main.py`


### Command line arguments

* `--rectangle`, `-r`: Draws the projection of the reference surface on the video frame as a blue rectangle.
* `--matches`, `-m`: Draws matches between reference surface and video frame.


## Troubleshooting

**If you get the message**:

```
Unable to capture video
```
printed to your terminal, the most likely cause is that your OpenCV installation has been compiled without FFMPEG support. Pre-built OpenCV packages such as the ones downloaded via pip are not compiled with FFMPEG support, which means that you have to build it manually.

## Explanation

See these excellent blog entries for an in-depth explanation of the logic behind the code:

* [Part 1](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/)
* [Part 2](https://bitesofcode.wordpress.com/2018/09/16/augmented-reality-with-python-and-opencv-part-2/)
