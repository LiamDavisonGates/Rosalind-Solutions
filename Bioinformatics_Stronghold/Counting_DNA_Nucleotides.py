#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title:   Counting DNA Nucleotides
Rosalind ID:     DNA
Rosalind #:      001
URL:             http://rosalind.info/problems/dna/
'''

with open('data/rosalind_dna.txt') as input_data:
    dna_string = input_data.read().strip()

    nucleotide_count = {}

    for nucleotide in dna_string:
        if nucleotide in nucleotide_count:
            nucleotide_count[nucleotide] += 1
        else:
            nucleotide_count[nucleotide] = 1

    print('{} {} {} {}'.format(nucleotide_count['A'],
                               nucleotide_count['C'],
                               nucleotide_count['G'],
                               nucleotide_count['T']))
