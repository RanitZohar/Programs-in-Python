# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vLuT1g8rzutHoR3nt1Qe_7sV0la4SnGV

# Ranit Zohar ,
#Aviah Miriam Yadler , 

targil2,misssion1-Imperative
"""

import math
L= list(range(101))
total = 0
for x in L:
		total+= math.pow(x,2)

print(total)

"""targil2,misssion1-Functional"""

import math
def pow(x):
	return math.pow(x, 2)
total=sum(map(pow ,range(1,101)))
print(total)

