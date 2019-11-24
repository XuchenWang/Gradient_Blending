'''
  File name: getIndexes.py
  Author: Xuchen Wang
  Date created: Sept 24, 2019
'''


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def getIndexes(mask, targetH, targetW, offsetX, offsetY):
	maskH, maskW = mask.shape
	indexes = np.zeros((targetH, targetW))
	index=1
	maskSpace = np.max(mask)
	for h in range(0, maskH):
		y = h + offsetY
		for w in range(0, maskW):
			x = w + offsetX
			if x < targetW and y < targetH and x >= 0 and y >= 0 and mask[h,w]==maskSpace:
				indexes[y,x] = index
				index += 1
	return indexes


# mask = np.array(Image.open('1_mask.png'))
# plt.imshow(mask)
# plt.show()
# indexes = getIndexes(mask,479, 600,386, 223)
# plt.imshow(indexes)
# plt.show()
