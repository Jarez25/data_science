# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

array = np.array([1,2,3,4,5,4,4])
arrayDes = np.array([3,5,2,4,1,0])
arrayUno = np.array([[1,2,3,4],[5,6,7,8]])
arrayDos = np.array([[9,10,11,12],[13,14,15,16]])

allArray = np.concatenate((arrayUno, arrayDos), axis=0)
newarray = np.array_split(array, 3)
x =  np.where(array == -1)
arrayDes1 = np.sort(arrayDes)



print(newarray)
print(x)
print(arrayDes)
print(arrayDes1)
