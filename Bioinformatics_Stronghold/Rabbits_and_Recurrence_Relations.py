#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title:   Rabbits and Recurrence Relations
Rosalind ID:     FIB
Rosalind #:      004
URL:             https://rosalind.info/problems/fib/
'''

with open('data/rosalind_fib.txt') as input_data:

    data = input_data.read().split()
    n = int(data[0])
    k = int(data[1])
    
    rabbits = [1,1]

    for x in range(2,n):
        rabbits.append((rabbits[x-2]*k) + rabbits[x-1])
    
    print(rabbits[-1])