with open('data/rosalind_rna.txt') as input_data:
    dna_string = input_data.read().strip()

    transcribe_dic = {'A':'A','G':'G','C':'C','T':'U'}
    rna_string = ''

    for nucleotide in dna_string:
        rna_string = rna_string + transcribe_dic[nucleotide]

    print(rna_string)
