# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 00:05:48 2021

@author: somak

Chapter 8
Strings
Think Python 2e Downey
"""

"==================================================================="
"""
function count takes a string and a letter as input arguments and 
returns the frequency of the letter in the string
"""

def count(string, letter):
    count=0
    for a in string:
        if a==letter:
            count+=1
    return count

"=================================================================="
"in_both function prints the letters common to two words"
def in_both(first_word, second_word):
    for letter in first_word:
        if letter in second_word:
            print(letter)
        
"================================================================="        

"""
Caesar cypher

inputs a string and rotates each letter by key steps
"""

def cypher(string, key):
    if(type(key)!=int or key<1 or key>26):
        print("Invalid input!")
        return None
    new_string=""
    for letter in string:
        if(ord(letter)>=65 and ord(letter)<=90):
            let=ord(letter)+key
            if let>90:
                let=let%90+64
            new_string+=chr(let)
        elif(ord(letter)>=97 and ord(letter)<=122):
            let=ord(letter)+key
            if let>122:
                let=let%122+96
            new_string+=chr(let)
        else:
            new_string+=letter
    return new_string
"================================================================"
"Decypher the Caesar cypher"

def decypher(string, key):
    if(type(key)!=int or key<1 or key>26):
        print("Invalid input!")
        return None
    new_string=""
    for letter in string:
        if(ord(letter)>=65 and ord(letter)<=90):
            let=ord(letter)-key
            if let<65:
                let+=26
            new_string+=chr(let)
        elif(ord(letter)>=97 and ord(letter)<=122):
            let=ord(letter)-key
            if let<97:
                let+=26
            new_string+=chr(let)
        else:
            new_string+=letter
    return new_string
"==============================================================="