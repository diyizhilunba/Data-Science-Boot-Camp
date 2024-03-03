# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 00:48:01 2024

@author: mayil
Write a function count_vowels(word) that 
takes a word as an argument and 
returns the number of vowels in the word
"""

def count_vowels(words):
    count = 0
    for word in words:
        if word.lower() in {'a','e','i','o','u'}:
            count += 1
    return count


print(count_vowels(''))
