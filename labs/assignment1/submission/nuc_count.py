#!/usr/bin/env python3

""" 
nuc_count.py counts nucleotides in a fasta file or a plain sequence

Usage: python3 nuc_count.py <fasta>

<fasta> = path to a fasta file
""" 

# Import modules
import sys

# sys.arg is a list containing 2 elements: the script name and 1 command line argument
# Check that all the command line argument was given. If not, print the documentation and exit.
if (len(sys.argv) != 2):
    sys.exit(__doc__) 

# Save the input arguments as variables
fasta = sys.argv[1]

# Initialize a nucleotide string
nucleotides = ""

# Load the fasta sequence
# NOTE: this script assumes there is only *one* sequence in the fasta file
# Open the fasta file
with open(fasta) as f:
    # For each line in the file
    for line in f:
        # Skip lines starting with ">"
        if not line.startswith(">"):
            # Add each line to the nucleotide string
            nucleotides += line.rstrip()

# Make the nucleotide string all capital letters 
nucleotides = nucleotides.upper()

# Count the nucleotides and print output
num_a = nucleotides.count('A')
num_c = nucleotides.count('C')
num_g = nucleotides.count('G')
num_t = nucleotides.count('T')
num_n = nucleotides.count('N')

print ("Raw Counts")
print ("A: ", num_a)
print ("C: ", num_c)
print ("G: ", num_g)
print ("T: ", num_t)
print ("N: ", num_n)


## Part 3
### Print out the frequencies for each nucleotide in alphabetical order
#Get the total number of nucleotides, ignore Ns
total_counts = num_a + num_c + num_g + num_t
freq_a = float(num_a)/total_counts
freq_c = float(num_c)/total_counts
freq_g = float(num_g)/total_counts
freq_t = float(num_t)/total_counts

#Print out the frequencies
print ("Frequencies")
print ("A: ", freq_a)
print ("C: ", freq_c)
print ("G: ", freq_g)
print ("T: ", freq_t)

## Part 5
dinuc_counts = {} #key is dinuc, value is count
total_count = 0.0 #Denom
for i, nuc in enumerate(nucleotides):
    if i != len(nucleotides) - 1: #Not the last nuc
        #Ignore N
        if nucleotides[i] == "N" or nucleotides[i+1] == "N":
            continue
        dinuc = nucleotides[i] + nucleotides[i+1]
        if dinuc not in dinuc_counts:
            dinuc_counts[dinuc] = 0
        dinuc_counts[dinuc] += 1
        total_count += 1

#print the counts
print(len(nucleotides))
print("Dinucleotide Frequencies")
for dinuc, count in dinuc_counts.items():
    print(dinuc, ":", round(count/total_count, 2))
