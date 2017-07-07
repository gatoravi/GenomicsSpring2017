#!/usr/bin/env python3
"""
Align sequencing reads to a set of genes.

Usage: map_sequence_starter.py <cDNA_fasta> <seq_reads_file>

Arguments:
    <cDNA_fasta>     = Path to cDNA fasta file.  (Required.)
    <seq_reads_file> = Path to sequencing reads file.  (Required.)
"""

import sys

def reverse_complement(sequence):
    #This function takes the reverse complement of a sequence

    #define complement dictionary
    complements = { 'A' : 'T',
                    'T' : 'A',
                    'G' : 'C',
                    'C' : 'G',
                    'N' : 'N'}

    #reverse the string
    revseq = sequence[::-1]
    revcomp = ""
    #take the complement
    for nuc in revseq:
        revcomp += complements[nuc]
    #return the reverse complement
    return revcomp

def read_cDNA_file_to_dict(filename):
    #This function reads a cDNA file into a dictionary.  
    #initialize dictionary
    cdnas = {}
    #open file
    with open(filename) as f1_fh:
        #loop through file
        for line in f1_fh:
            #remove newline
            line = line.rstrip("\n")
            #get gene name
            if line[0] == ">":
                gene = line.split("|")[1] 
                #print("gene", gene)
                continue
            #read in sequence
            sequence = line.upper()
            #print("sequence", sequence)
            #put name and sequence in dictionary
            cdnas[gene] = sequence
    #return dictionary
    return cdnas


def create_twenty_five_mer_dict(cDNA_dict):
    #This function creates a dictionary of 25mer sequences from the cDNA sequences.  Thedictionary keys are the 25mer sequences and the values are the corresponding gene names.   
    #initialize dictionary
    twentyfivemers = {}
    #loop through cDNA dictionary
    for gene in cDNA_dict:
        #get sequence that corresponds to the key
        sequence = cDNA_dict[gene]
        #print(gene, sequence)
        #move through sequence, grabbing 25 mers and create dictionary
        for i in range(0, len(sequence) - 25 + 1):
            kmer = sequence[i:i+25]
            twentyfivemers[kmer] = gene
    #return dictionary
    return twentyfivemers

##############main loop###################

#parse command line
#check that the correct number of arguments were given
if (len(sys.argv) != 3):
    sys.exit(__doc__)

cDNA_file = sys.argv[1]
seq_reads_file = sys.argv[2]

#read in cDNAs
cDNA_dict = read_cDNA_file_to_dict(cDNA_file)
print("Read in the cDNAs")


twenty_five_mer_dict = create_twenty_five_mer_dict(cDNA_dict)
print("Created dictionary")


count_dict = {}
for key in cDNA_dict:
    count_dict[key] = 0


fh = open(seq_reads_file, "r")

for line in fh:

    line = line.rstrip()
    line = line.upper() 
    if line in twenty_five_mer_dict.keys(): 
        if twenty_five_mer_dict[line] in count_dict.keys():
            count_dict[twenty_five_mer_dict[line]] = count_dict[twenty_five_mer_dict[line]] + 1

    else: 
        rc_seq = reverse_complement(line)
        if rc_seq in twenty_five_mer_dict.keys(): 
            if twenty_five_mer_dict[rc_seq] in count_dict.keys():
                count_dict[twenty_five_mer_dict[rc_seq]] = count_dict[twenty_five_mer_dict[rc_seq]] + 1

fh.close()

print("Name\tReads\tReads per BP")
for name, count in sorted(count_dict.items()):
    print(name + "\t" + str(count) + "\t" + str(float(count)/len(cDNA_dict[name])))
