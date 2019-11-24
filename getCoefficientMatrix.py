'''
  File name: getCoefficientMatrix.py
  Author: Xuchen Wang
  Date created: Sept 24, 2019
'''

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import getIndexes

def getCoefficientMatrix(indexes):
	N = int(np.max(indexes))
	coeffA = np.zeros((N,N))

	for h in range(0,indexes.shape[0]):
		for w in range(0,indexes.shape[1]):
			index = int(indexes[h,w])-1
			if index>=0:
				coeffA[index, index] = 4
				for pt in getNeighbors(indexes, h,w):
					coeffA[index,pt] = -1

	return coeffA


def getNeighbors(indexes, h,w):
	neighList = []
	if h-1>=0 and indexes[h-1,w] > 0: neighList.append(int(indexes[h-1,w])-1)
	if h+1<indexes.shape[0] and indexes[h+1,w] > 0: neighList.append(int(indexes[h+1,w])-1)
	if w+1<indexes.shape[1] and indexes[h,w+1] > 0: neighList.append(int(indexes[h,w+1])-1)
	if w-1>=0 and indexes[h,w-1] > 0: neighList.append(int(indexes[h,w-1])-1)
	return neighList

# mask = np.array(Image.open('1_mask.png'))
# indexes = getIndexes.getIndexes(mask,479, 600,386, 223)
# plt.imshow(indexes)
# plt.show()
# coeffA = getCoefficientMatrix(indexes)
# plt.imshow(coeffA)
# plt.show()
