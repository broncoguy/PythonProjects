# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:23:53 2020

@author: Larry
"""

def split(word): 
    return [char for char in word]  

def translate(x):
    C = 100
    D = 500
    M = 1000 
    I = 1
    II = 1 + 1
    III = 1 + 1 + 1
    IV = 5 - 1
    V = 5
    VI = 5 + 1
    VII = 5 + 1 + 1
    VIII = 5 + 1 + 1 + 1
    IX = 10 - 1
    X = 10
    L = 50
    XC = C - X
       
    if(x == 'I'):
        return I
    elif(x == 'II'):
        return II
    elif(x == 'III'):
        return III
    elif(x == 'IV'):
        return IV
    elif(x == 'V'):
        return V
    elif(x == 'VI'):
        return VI
    elif(x == 'VII'):
        return VII
    elif(x == 'VIII'):
        return VIII
    elif(x == 'IX'):
        return IX
    elif(x == 'X'):
        return X
    elif(x == 'L'):
        return L
    elif(x == 'XC'):
        return XC
    elif(x == 'C'):
        return C
    elif(x == 'D'):
        return D
    elif(x == 'M'):
        return M
    else:
        return False


RN = input("Enter Roman numeral : ") 
x = split(RN)
total  = 0

if(translate(RN) == False):
    for i in range(len(x)):
        total = total + translate(x[i])
else:
    total = translate(RN)


print(total)

