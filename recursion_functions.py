# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 00:33:16 2021

@author: somak


contains a bunch of recursive functions 
that I worked on from: 
Think Python 2e - Allen B. Downey
Chapter 6

List:
    factorial
    factorial_scaffold
    fibonacci
    gcd
    is_palindrome
    ackermann
"""

"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
"""
factorial function

n!=n.(n-1)!= n.(n-1).....3.2.1
"""

def factorial(n):
    if (n<1):
        print("Only n>=1 please!")
        return None
    if n==1:
        return 1
    return factorial(n-1)*n

"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
"""
Factorial with scafolding
This displays the recursive calls of the function

This function has also been upgraded to check if the input
is integer or not.

On case it is not an integer it outputs an error message
"""

def factorial_scaffold(n):
    if not isinstance(n, int):
        print("Only integers please!")
        return None
    elif n<0:
        print("Only positive integers please!")
        return None
    elif n==0:
        print("factorial "+str(n))
        print("returning 1")
        return 1
    else:
        space=' '*(2*n)
        print(space,"factorial "+str(n)+" ...")
        value=n*factorial_scaffold(n-1)
        print(space, "returning " + str(value))
        return value
        
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
"""
Greatest common divisor:
    gcd(a,b) is the greatest positive integer that divides
    both a and b.
    We assume that a and b are both positives.
    
Number theory tells us:
    gcd(a,b)=gcd(b,r) where r=a mod b assuming a>=b

Base case:
    gcd(a,0)=a
    
"""

def gcd(a,b):
    if a<0 or b<0:
        print("Positive numbers please!")
        return None
    elif(min(a,b)==0):
        return max(a,b)
    else:
        r=max(a,b)%min(a,b)
        return gcd(min(a,b),r)
    

"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
"""
Fibonacci sequence:
    1 1 2 3 5 8 13 ....
"""

def fibonacci(n):
    if n<1:
        print("Invalid input for number of terms!")
        return None
    
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"        

"""
Palindrome:
    A word spelt the same as backwards
    
"""
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word)==0:
        return True
    else:
        return is_palindrome(middle(word)) and first(word)==last(word)
    
    
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

"""
Ackermann function:
    A(m,n)=:
        n+1                if m=0
        A(m-1,1)           if m>0 and n=0
        A(m-1,A(m,n-1))    if m>0 and n>0
"""

def ackermann(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackermann(m-1,1)
    elif m>0 and n>0:
        return ackermann(m-1, ackermann(m,n-1))
    else:
        print("Invalid result")
        return None
    
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"