#!/usr/bin/env python3
"""Scan a DNA sequence to find putative binding sites

Usage: python3 scan_sequence.py <scoring_matrix> <sequence_file> <score_threshold>

Args:
    scoring_matrix = Path to scoring matrix. The rows of the matrix correspond 
       to A, C, G, and T, and the columns correspond to positions
    sequence_file = Path to DNA sequence file.
    score_threshold = Only substrings which have a score >= threshold will be output
"""
import sys

# Helper dictionary for reverse complementation
reverse_comp = { 'A':'T', 'C':'G', 'G':'C', 'T':'A' }

###############################################################
# Begin functions
###############################################################

def create_scoring_matrix_from_file(matrix_file):
    """Read the scoring matrix from a file and store in a dictionary.
    """
    file_data = [ x.split() for x in open(matrix_file).readlines() ]
    scoring_matrix = [ dict(A=float(a_score), C=float(c_score), G=float(g_score), 
        T=float(t_score)) for a_score, c_score, g_score, t_score in 
        zip(file_data[0], file_data[1], file_data[2], file_data[3])
    ]

    return scoring_matrix


def read_sequence_from_file(file_name):
    """Read the DNA sequence from a file and store in a string
    """
    return open(file_name).readlines()[0].strip()



def score_with_matrix(subseq, matrix):
    """Given a subsequence and a scoring matrix, compute the score using
    the matrix by scanning the subsequence. Sum across all positions.
    """
    return sum([ score[ base ] for score, base in zip(matrix, subseq)])


def get_reverse_complement(in_string):
    """Given a DNA string compute it's reverse complement
    """
    return (''.join([ reverse_comp[x] for x in in_string[::-1] ]))

###############################################################
# End functions
###############################################################

###############################################################
# Begin main script
###############################################################

# Check the correct number of command line arguments
if(len(sys.argv)!= 4):
    sys.exit(__doc__)

score_matrix_file = sys.argv[1]
sequence_file = sys.argv[2]
score_threshold = float(sys.argv[3])

#Read the scoring matrix file
score_matrix = create_scoring_matrix_from_file(score_matrix_file)
#get the length of the subsequence
motif_width = len(score_matrix)
#get the sequence to scan
search_sequence = read_sequence_from_file(sequence_file)

# Calculate the number of matrix 'windows' for calculating
# sequence scores
last_index = len(search_sequence) - motif_width + 1

# Go through the sequence and compute the score for each subsequence of length motif_width
# The result is a list of tuples with the position and score
forward_hit_list = [ (i, score_with_matrix(search_sequence[i:i+motif_width], score_matrix)) for i in range(last_index) if score_with_matrix(search_sequence[i:i+motif_width], score_matrix) >= score_threshold]

# Go through all the hits and print the ones that pass the threshold
if len(forward_hit_list) == 0:
    print("No threshold-exceeding hits found in the forward direction!")
else:
    print("orientation\tposition\tsequence\tscore")
    for hit in forward_hit_list:
        print("forward\t{position:d}\t{sequence:s}\t{score:.2f}".format(position=hit[0],
              sequence = search_sequence[hit[0]:hit[0]+motif_width], score=hit[1]))

#get the sequence to scan
reverse_search_sequence = get_reverse_complement(search_sequence)
# Go through the sequence and compute the score for each subsequence of length motif_width
# The result is a list of tuples with the position and score
reverse_hit_list = [ (i, score_with_matrix(reverse_search_sequence[i:i+motif_width], score_matrix)) for i in range(last_index) if score_with_matrix(reverse_search_sequence[i:i+motif_width], score_matrix) >= score_threshold]

# Go through all the hits and print the ones that pass the threshold
if len(reverse_hit_list) == 0:
    print("No threshold-exceeding hits found in the reverse direction!")
else:
    for hit in reverse_hit_list:
        print("reverse\t{position:d}\t{sequence:s}\t{score:.2f}".format(position=hit[0],
              sequence = reverse_search_sequence[hit[0]:hit[0]+motif_width], score=hit[1]))
