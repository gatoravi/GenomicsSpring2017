#!/usr/bin/env python3

"""make_seq.py prints a random sequence given a sequence length and nucleotide frequencies.  The random sequence will have the same nucleotide frequencies as the input nucleotide frequencies.

Usage: python3 make_seq.py <sequence_length> <a_freq> <c_freq> <g_freq> <t_freq>

<sequence_length> = Length of sequence to generate
<a_freq> = frequency of As
<c_freq> = frequency of Cs
<g_freq> = frequency of Gs
<t_freq> = frequency of Ts
"""

# Import modules 
import sys
import random

# sys.arg is a list containing 6 elements: the script name and 5 command line arguments
# Check that all 5 command line arguments were given. If not, print the documentation and exit.
if (len(sys.argv) != 6):
	sys.exit("ERROR: incorrect number of arguments.\n" + __doc__) 

# Save the input arguments as variables
# By default, the command line arguments are saved as strings. Convert them to numeric types.
sequence_length = int(sys.argv[1])
a_freq = float(sys.argv[2])
c_freq = float(sys.argv[3])
g_freq = float(sys.argv[4])
t_freq = float(sys.argv[5])

# Check that frequencies add to 1. If not, exit the program 
if (abs(a_freq + t_freq + c_freq + g_freq - 1) > 1e-4):
	sys.exit("ERROR: Nucleotide frequencies do not add up to 1!")

## Part 4
### TODO Generate a random nucleotide sequence

# Initialize an empty string that nucleotides can be appended to
output_seq = ""

#Cumulative nucleotide freqs
freq_cutoffs = [0, a_freq, a_freq + c_freq, a_freq + c_freq + g_freq, a_freq + c_freq + g_freq + t_freq]
nucs = ["A", "C", "G", "T"]

#Create a for loop that will be repeated <sequence_length> times
for i in range(0, sequence_length):
	#Generate a random float between 0 and 1
	p = random.random()
	#Get the corresponding nucleotide
	for i in range(1, 5):
		#See which bin p falls in and select the corresponding nuc
		if p > freq_cutoffs[i-1] and p <= freq_cutoffs[i]:
			random_nuc = nucs[i - 1]
			#Append the nucleotide to the nucleotide sequence
			output_seq += random_nuc

# Print the full nucleotide sequence
print(output_seq)


