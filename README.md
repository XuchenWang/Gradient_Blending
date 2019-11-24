# Xuchen Wang - CIS 581 Project 1b

This project uses gradient blending to combine two images together.

## Getting Started

The folder contains pictures and scripts: 

"1_Blend.jpg" is the blending result of the provided source image, "1_source.jpg", and the provided background image, "1_background.jpg". "2_source.jpg" and "2_background.jpg" are my own source image and background image, respectively. Their result is also included in the folder, named "2_Blend.jpg". 

For scripts, createMask.py, drawMask.py, and maskImage.py are the mask python file provided by the TA. gradientBlending.py contains the main function, which calls seamlessCloningPoisson.py and starts the whole blending process. Each of the rest python files involves part of the blending process, like get indexes, get coefficient matrix, etc.

## Running the tests

Direct the terminal to the folder. Simply running gradientBlending.py with the source image, target image, offsets (X and Y axis). The function will first ask the user choose the area from the source image and then start blending. Sample termimal commands are as following:

```
python3 gradientBlending.py --bg '1_background.jpg' --fg '1_source.jpg' --oX 200 --oY 200 

python3 gradientBlending.py --bg '2_background.jpg' --fg '2_source.jpg' --oX 590 --oY 200
```

## Acknowledgments

* Collaberated with Yuezhan Tao for this project.

