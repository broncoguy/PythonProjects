# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:02:56 2020

@author: Larry
"""

def singledigit(x):
    if(x == '1'):
        stringNumber.append("one")
    elif(x == '2'):
        stringNumber.append("two")
    elif(x == '3'):
        stringNumber.append("three")
    elif(x == '4'):
        stringNumber.append("four")
    elif(x == '5'):
        stringNumber.append("five")
    elif(x == '6'):
        stringNumber.append("six")
    elif(x == '7'):
        stringNumber.append("seven")
    elif(x == '8'):
        stringNumber.append("eight")
    elif(x == '9'):
        stringNumber.append("nine")
    elif(x == '0'):
        stringNumber.append("Zero") 
def teendigit(x):
    if(x == '10'):
        stringNumber.append("ten")
    elif(x == '11'):
        stringNumber.append("eleven")
    elif(x == '12'):
        stringNumber.append("twelve")
    elif(x == '13'):
        stringNumber.append("thirteen")
    elif(x == '14'):
        stringNumber.append("fourteen")
    elif(x == '15'):
        stringNumber.append("fifteen")
    elif(x == '16'):
        stringNumber.append("sixteen")
    elif(x == '17'):
        stringNumber.append("seventeen")
    elif(x == '18'):
        stringNumber.append("eighteen")
    elif(x == '19'):
        stringNumber.append("nineteen")
    else:
        pass        
def doubledigit(x):
    if(x == '2'):
        stringNumber.append("twenty")   
    elif(x == '3'):
        stringNumber.append("thirty")
    elif(x == '4'):
        stringNumber.append("fourty")
    elif(x == '5'):
        stringNumber.append("fifty")
    elif(x == '6'):
        stringNumber.append("sixty")
    elif(x == '7'):
        stringNumber.append("seventy")
    elif(x == '8'):
        stringNumber.append("eighty")
    elif(x == '9'):
        stringNumber.append("ninety") 
    else:
        singledigit(x)         
def hundred():
    stringNumber.append("hundred")      
def thousand():
    stringNumber.append("thousand")    
def million():
    stringNumber.append("million")
def billion():
    stringNumber.append("billion")
          
i = 0

def Threedigit(number):
    length = len(str(number))
    for i in range(length):
        x = number[i:i+1]
        y = number[i:i+2]
        y_number = int(y)
        if(length == 1):
            if(x != '0'):
                singledigit(x)
                length -= 1
            elif(number == '0'):
                singledigit(x)
            else:
                length -= 1
        elif(length == 2):
            if(y_number > 9 and y_number < 20):
                teendigit(y)
                length -= 2
            elif(x != '0'):
                doubledigit(x)
                length -= 1
            else:
                length -= 1
        elif(length == 3):
            if(x != '0'):
                singledigit(x)
                hundred()
                length -= 1
            else:
                length -= 1 

input_number = input("Enter Number: ")   
size = len(str(input_number))
stringNumber = []
if(size <= 3):
    Threedigit(input_number)
elif(size == 4):
    Threedigit(input_number[0:1])
    thousand()
    Threedigit(input_number[1:4])
elif(size == 5):
    Threedigit(input_number[0:2])
    thousand()
    Threedigit(input_number[2:5])
elif(size == 6):
    Threedigit(input_number[0:3])
    thousand()
    Threedigit(input_number[3:6])
elif(size == 7):
    Threedigit(input_number[0:1])
    million()
    Threedigit(input_number[1:4])
    if(input_number[1:4] != '000'):
        thousand()
    else:
        pass
    Threedigit(input_number[4:7])
elif(size == 8):
    Threedigit(input_number[0:2])
    million()
    Threedigit(input_number[2:5])
    if(input_number[2:5] != '000'):    
        thousand()
    else:
        pass
    Threedigit(input_number[5:8])
elif(size == 9):
    Threedigit(input_number[0:3])
    million()
    Threedigit(input_number[3:6])
    if(input_number[3:6] != '000'):
        thousand()
    else:
        pass
    Threedigit(input_number[6:9])
elif(size == 10):
    Threedigit(input_number[0:1])
    billion()
    Threedigit(input_number[1:4])
    if(input_number[1:4] != '000'):    
        million()
    else:
        pass
    Threedigit(input_number[4:7])
    if(input_number[4:7] != '000'):
        thousand()
    else:
        pass
    Threedigit(input_number[7:10])    
    
for i in range(len(stringNumber)):
    print(stringNumber[i],end = " ")
  
    
