# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 00:55:42 2024
Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
@author: mayil
"""

for num in range(1,21):
    parity = "odd" if (num % 2 == 1) else "even"
    print(num, ":", parity)