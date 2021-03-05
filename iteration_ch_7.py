# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:07:07 2021

@author: somak
"""
import pandas as pd
import math

def mysqrt(a):
    if a<0:
        print('Only non-negative number please!')
        return None
    err=1
    x=1
    x1=-1
    while err>1e-15:
        x = (x+a/x)/2
        err=abs(x-x1)
        x1=x
    return x


def mytable(a):
    print("a    | mysqrt(a)           | math.sqrt(a)        | diff")
    print("-----|---------------------|---------------------|---------------------------")
    for i in range(1,a+1):
        string=str(float(i))
        string+=(5-len(str(float(i))))*" "+"| "
        string+=str(mysqrt(i))
        string+=(20-len(str(mysqrt(i))))*" "+"| "
        string+=str(math.sqrt(i))
        string+=(20-len(str(math.sqrt(i))))*" "+"| "
        string+=str(abs(mysqrt(i)- math.sqrt(i)))
        print(string)

    
"""   
"Pandas application"
"Did not turn out well"
"Maybe in time"

"""

""" 
def table(a):
    list_a=[]
    list_mysq=[]
    list_math_sq=[]
    diff=[]
    for i in range(1,a+1):
        list_a.append(float(i))
        list_mysq.append(mysqrt(i))
        list_math_sq.append(math.sqrt(i))
        diff.append(abs(mysqrt(i)- math.sqrt(i)))
    dictionary={'a': list_a,
                'mysqrt(a)': list_mysq,
                'math.sqrt(a)': list_math_sq,
                'diff': diff}    
    "print(dictionary)"
    df=pd.DataFrame(dictionary)
    df.set_index('a')
    display(df)
"""

"""
Calculates factorial for a positive number
"""

def fact(n):
    fact=1;
    for i in range(int(n)):
        fact*=(i+1)
    return fact

def ramanujan():
    k=0
    remainder=1
    inv_pie=0
    while(remainder>1e-5):
        remainder=(2*mysqrt(2)/9801)*((fact(4*k)*(1103+26390*k))/(((fact(k))**4)*(396)**(4*k)))
        inv_pie+=remainder
        k+=1
    return 1/inv_pie
