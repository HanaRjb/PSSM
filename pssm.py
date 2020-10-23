# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:59:23 2020

@author: hana
"""
import re, sys, os
from collections import Counter
pPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(pPath)
import readFasta
import checkFasta
import numpy as np
import pandas as pd

#PYTHON PROGRAM FOR CREATING A PSSM MATRIX
import math
def PSSM(fastas, **kw):
    AA ="ACDEFGHIKLMNPQRSTVWY"
    encodings = []
    code=[]
    q=[]
    temp=0
    for i in fastas:
        name, sequence = i[0], i[1]
        temp=temp+1
        encodings.append(sequence)
    n=len(encodings)
    s1=encodings[0]
    l=len(s1)
    #sc=[[0.0 for i in range(l*4)] for j in range(len(AA)*4)]
    for i in range(l):
        for j in range(len(AA)):
            m=1
            for k in range(n):
                if(AA[j]==encodings[k]):
                    m=m+1
                v=m/(20+n)
                sc=(math.log(v/0.05))/math.log(10)
                code.append('%2.3f'%sc)
        q.append(code)
    return q
    
    


                    
		   


kw=  {'path': r"H_train.txt",'order': 'ACDEFGHIKLMNPQRSTVWY'}   
fastas1 = readFasta.readFasta(r"H_train.txt")

result=PSSM(fastas1, **kw)

data1=np.matrix(result[1:])[:,1:]
#data_=pd.DataFrame(data=data1)
#data_.to_csv('pssm_H_train.csv')