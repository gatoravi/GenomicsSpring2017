"""
Calculates the fraction of wobble positions that
are conserved.
    Usage: python3 neutral_rate.py <clustalw alignment file> <min_bp_conserved> <window_length>
"""

import sys

#Store the aligned sequence for each species
species_sequences = {}

#Print usage
def usage():
    print("python3 neutral_rate.py <clustalw alignment file> <min_bp_conserved> <window_length>")

#Process the alignment file
def process_aln(alignment_file):
    "Process the alignment file"
    #Open alignment file
    with open(alignment_file) as afh:
        #Go through file
        for line in afh:
            line = line.rstrip("\n")
            #Split columns
            fields = line.split()
            #Print out sequence lines
            if len(fields) != 2:
                continue
            #Get the fields
            species = fields[0]
            sequence = fields[1]
            #Check if sequence exists for species
            if species not in species_sequences:
                species_sequences[species] = ""
            #Append the sequence to this species
            species_sequences[species] += sequence

def look_at_conserved():
    #Get all the species
    species = list(species_sequences.keys())
    sequences = list(species_sequences.values())
    start_frame = False
    conserved = 0
    not_conserved = 0
    i = 0
    while i < len(sequences[0]) - 2:
        #initialize start to false
        start = True
        #Look at all 4 sequences
        for sequence in sequences:
            #Look for start codon
            codon = sequence[i:i+3]
            if codon != "ATG":
                start = False
        #Look at codons within frame
        if start_frame:
            #Look at wobble position
            if sequences[0][i+2] == sequences[1][i+2] == sequences[2][i+2] == sequences[3][i+2]:
                conserved += 1
            else:
                not_conserved += 1
        #Start ORF
        if not start_frame and start:
            start_frame = True
        if start_frame:
            i += 3 #Found the starting frame
        else:
            i += 1 #Haven't found the starting frame
    print("Fraction conserved:", conserved/(conserved + not_conserved))

#See if each 10 b.p window is conserved
def get_conserved_subwindows(sequences, i, window_size, min_bp_conserved):
    for j in range(window_size - 10 + 1):
        #number of conserved bases in the window
        conserved = 0
        #Look at all possible 10-mers
        for k in range(10):
            if sequences[0][i+j+k] == sequences[1][i+j+k] == sequences[2][i+j+k] == sequences[3][i+j+k]:
                conserved += 1
        #not greater than minimum match
        if conserved < min_bp_conserved:
            return False
    #True if all 10-mers greater than min match
    return True

#Get the conserved windows
def get_conserved_windows(min_bp_conserved, window_size):
    sequences = list(species_sequences.values())
    print(sequences[0][0:706])
    i = 0
    #Output file
    with open("S_cer_conserved.txt", "w") as sfh:
        #Header
        print("Start", "Stop", "Sequence", file = sfh)
        while i < 706 - window_size + 1:
            #initialize start to false
            start = True
            #Look at all 4 sequences
            if get_conserved_subwindows(sequences, i, window_size, min_bp_conserved):
                print(i, i + window_size, sequences[2][i:i+window_size], file = sfh)
            i += window_size

#main function
def main():
    "Everything starts here"
    if len(sys.argv) != 4:
        return usage()
    #Parse arguments
    alignment_file = sys.argv[1]
    min_bp_conserved = int(sys.argv[2])
    window_size = int(sys.argv[3])
    #Process the file
    process_aln(alignment_file)
    #Look at wobble positions
    look_at_conserved()
    #Get teh conserved windows
    get_conserved_windows(min_bp_conserved, window_size)

main()
