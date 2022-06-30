#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title:   Complementing a Strand of DNA
Rosalind ID:     REVC
Rosalind #:      003
URL:             https://rosalind.info/problems/revc/
'''

with open('data/rosalind_revc.txt') as input_data:
    dna_string = input_data.read().strip()

    compliment_dic = {'A':'T','G':'C','C':'G','T':'A'}
    compliment_string = ''

    for nucleotide in dna_string[::-1]:
        compliment_string = compliment_string + compliment_dic[nucleotide]

    print(compliment_string)
