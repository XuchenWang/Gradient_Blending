'''
  File name: reconstructImg.py
  Author:Xuchen Wang
  Date created: Sept 24, 2019
'''


import numpy as np

def reconstructImg(indexes, red, green, blue, targetImg):
    h = indexes.shape[0]
    w = indexes.shape[1]
    for i in range(0, h):
        for j in range(0, w):
            if indexes[i][j]>0:
                targetImg[i,j,0] = red[(int(indexes[i,j])-1)]
                targetImg[i,j,1] = green[(int(indexes[i,j])-1)]
                targetImg[i,j,2] = blue[(int(indexes[i,j])-1)]
    return targetImg

# def reconstructImg(indexes, red):
#     h = indexes.shape[0]
#     w = indexes.shape[1]
#     for i in range(0, h):
#         for j in range(0, w):
#             if indexes[i][j]>0:
#                 indexes[i,j] = red[(int(indexes[i,j])-1)]
#     return indexes
