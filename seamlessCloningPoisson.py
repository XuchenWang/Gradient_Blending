'''
  File name: seamlessCloningPoisson.py
  Author: Xuchen Wang
  Date created: Sept 24, 2019
'''

import getIndexes, getCoefficientMatrix, getSolutionVect, reconstructImg
import numpy as np

from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import scipy.signal as signal

def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):
	# create index mask and coeffA
    indexes = getIndexes.getIndexes(mask, targetImg.shape[0], targetImg.shape[1],offsetX,offsetY)
    coeffA = getCoefficientMatrix.getCoefficientMatrix(indexes)


	# for Red channel
    print('r channel')
    sourceImg_R = sourceImg[:,:,0]
    targetImg_R = targetImg[:,:,0]
    solVectorb_R = getSolutionVect.getSolutionVect(indexes, sourceImg_R, targetImg_R, offsetX, offsetY)
    x_R = np.linalg.solve(coeffA, solVectorb_R)
    x_R = np.clip(x_R,0,255)
    # print(len(x_R))


	# for Green channel
    print('g channel')
    sourceImg_G = sourceImg[:,:,1]
    targetImg_G = targetImg[:,:,1]
    solVectorb_G = getSolutionVect.getSolutionVect(indexes, sourceImg_G, targetImg_G, offsetX, offsetY)
    x_G = np.linalg.solve(coeffA, solVectorb_G)
    x_G = np.clip(x_G,0,255)

    # for Blue channel
    print('b channel')
    sourceImg_B = sourceImg[:,:,2]
    targetImg_B = targetImg[:,:,2]
    solVectorb_B = getSolutionVect.getSolutionVect(indexes, sourceImg_B, targetImg_B, offsetX, offsetY)
    x_B = np.linalg.solve(coeffA, solVectorb_B)
    x_B = np.clip(x_B,0,255)

    print('reconstructing')
    resultImg = reconstructImg.reconstructImg(indexes, x_R, x_G, x_B, targetImg)
    return resultImg


# targetImg = np.array(Image.open('2_background.jpg'))
#
# # plt.imshow(targetImg)
# # plt.show()
# mask = np.array(Image.open('2_mask.png'))
# # plt.imshow(mask)
# # plt.show()
# sourceImg = np.array(Image.open('2_source.jpg'))
# # plt.imshow(sourceImg)
# # plt.show()
# resultImg= seamlessCloningPoisson(sourceImg, targetImg, mask, 590, 200)
# plt.imshow(resultImg)
# plt.show()
