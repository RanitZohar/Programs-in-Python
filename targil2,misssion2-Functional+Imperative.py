# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M5YdffgGz9oHYkl1BxRqF9q0aWXkZc20

# Ranit Zohar ,
#Aviah Miriam Yadler 

#targil2,mission2, Functional
"""

from multiprocessing import Pool
import time
import math
L=[range(101)]
tic= time.time()

def pow(x):
    return math.pow(x, 2)

with Pool(processes=2) as pool:
	c1= sum(pool.map(pow ,range(1,51)))
	c2= sum(pool.map(pow ,range(51,101)))
toc= time.time()

print(c1+c2)
print((toc-tic)*1000)

"""#targil2,mission2, Imperative"""

from multiprocessing import Pool
import time
import math
L=[range(101)]
tic= time.time()
total=0

def pow(x):
    return math.pow(x, 2)

with Pool(processes=2) as pool:
        for i in range(1,51):
            total+= pow(i)
        for i in range(51, 101):
            total+= pow(i)
toc= time.time()	
print(total)
print((toc-tic)*1000)