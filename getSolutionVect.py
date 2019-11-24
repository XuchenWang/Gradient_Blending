'''
  File name: getSolutionVect.py
  Author: Xuchen Wang
  Date created: Sept 24, 2019
'''

import numpy as np
import scipy.signal as signal

def getSolutionVect(indexes, source, target, offsetX, offsetY):
	N = int(np.max(indexes))
	SolVectorb1 = np.zeros(N)
	SolVectorb2 = np.zeros(N)

	laplacian = [[0,-1,0],[-1,4,-1],[0,-1,0]]
	source_lap = signal.convolve2d(source,laplacian,'same')

	for h in range(0, indexes.shape[0]):
		for w in range(0, indexes.shape[1]):
			index = int(indexes[h,w])-1
			if index>=0:
				b_1 = source_lap[h-offsetY, w-offsetX]
				b_2 = 0
				for j,i in get_neighbor(indexes, h, w):
					if indexes[j,i]==0:
						b_2=b_2+target[j,i]
				SolVectorb1[index] = b_1
				SolVectorb2[index] = b_2

	SolVectorb = SolVectorb1 + SolVectorb2
	return SolVectorb



def get_neighbor(indexes, y, x):
	neighbor = []
	if y-1>=0: neighbor.append((y-1, x))
	if x-1>=0: neighbor.append((y, x-1))
	if y+1<indexes.shape[0]: neighbor.append((y+1, x))
	if x+1<indexes.shape[1]: neighbor.append((y, x+1))
	return neighbor

# def laplace_pixel(source, indexes, y, x):
#     value = 4*source[y,x]
#     for j,i in get_neighbor(indexes, y, x):
#         value = value - source[j, i]
#     return value
