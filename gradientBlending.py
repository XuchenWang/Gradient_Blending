'''
  File name: seamlessCloningPoisson.py
  Author: Xuchen Wang
  Date created: Oct 1, 2019
'''

import argparse
import seamlessCloningPoisson
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import createMask

def main(background, foreground, offsetX, offsetY):
    background = background
    foreground = foreground

    bgImg = np.array(Image.open(background))
    fgImg = np.array(Image.open(foreground))
    maskImg = createMask.main(foreground)

    resultImg = seamlessCloningPoisson.seamlessCloningPoisson(fgImg, bgImg, maskImg, offsetX, offsetY)
    plt.imshow(resultImg)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bg", type=str, default=0, help="image path")
    parser.add_argument("--fg", type=str, default=0, help="image path")
    parser.add_argument("--oX", type=int, default=0, help="offsetX")
    parser.add_argument("--oY", type=int, default=0, help="offsetY")
    opt = parser.parse_args()
    main(background = opt.bg, foreground = opt.fg, offsetX=opt.oX, offsetY=opt.oY)
