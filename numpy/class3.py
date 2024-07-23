# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

arrayDos = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]] ])

#print(arrayDos)

for matirz in arrayDos:
    for fila in matirz:
        #for dato in fila:
         #   print(dato)
        print(fila)

#arrayDos = arrayDos.reshape(4,2)

#print(arrayDos)
#print(np.shape(arrayDos))