# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:18:57 2021

@author: somak

Word Play
Chapter 9
Think Python
2e
Downey
"""

"==================================================================="
def read(a):
    fin=open(a)
    for line in fin:
        print(line)
    return None
"==================================================================="

def read_strip(a):
    fin=open(a)
    for line in fin:
        word=line.strip()
        print(word)
    return None
        
"==================================================================="
"""
Lines with k characters
"""
def read_k_long(a,k):
    fin=open(a)
    for line in fin:
        word=line.strip()
        if len(word)>k:
            print(word)
        return None

'===================================================================='

"""
only select words fro 'file' which does not contain
the given character 'letter'
"""
def has_no(file, letter):
    fin=open(file)
    for line in fin:
        word=line.strip()
        if not(letter in word):
            print(word)
    return None
    
"===================================================================="
"""
function avoids takes a word and a string and returns TRUE if
the word does not use any of the letters in the string
"""
def avoids(word, string):
    for char in string:
        if char in word:
            return False
    return True


"""
avoids_ui takes a string from the user and prints all words
in a file that avoids the letters in the string
"""
def avoids_ui(file):
    text=input("Input string to avoid : ")
    fin=open(file)
    for line in fin:
        if avoids(line,text):
            print(line)
    return None
"===================================================================="    

"""
uses_only
takes a word and a string and returns TRUE if word contains
only letters in the string
"""

def uses_only(word,string):
    for char in word:
        if not(char in string):
            return False
    return True
"===================================================================="

"""
uses_all
takes a word and a string of required letters 
and returns TRUE if the word uses 
all the required letters at least once
"""

def uses_all(word,string):
    return uses_only(string,word)
"===================================================================="

"""
is_abecedarian
returns TRUE if the letters in a word appear in alphabetical order
(double letters are okay)
"""

def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i]>word[i+1]:
            return False
    return True
"===================================================================="   
"""
following function checks if a word has three cosequtive double letters
"""
def is_three_consecutive_doubles(word):
    if len(word)<6:
        return False
    for i in range(len(word)-5):
        if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True
    return False


"""
following function finds words from words.txt
that have three consecutive doubles
"""
def find_three_consecutive_doubles(a):
    fin=open(a)
    for line in fin:
        if is_three_consecutive_doubles(line):
            print(line)
    return None


"======================================================================"
"""
Exercise 9-8
"""
def is_reverse(word1,word2):
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[len(word2)-1-i]:
            return False
    return True


def is_palindrome(word):
    return is_reverse(word,word)    


def find_odo_read():
    for i in range(100000,999997):
        odo1=str(i)[3:]
        odo2=str(i+1)[1:]
        odo3=str(i+2)[1:5]
        odo4=str(i+3)
        if is_palindrome(odo1) and is_palindrome(odo2) and is_palindrome(odo3) and is_palindrome(odo4):
            print(str(i))
    return None
"====================================================================="    