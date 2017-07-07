#!/usr/bin/env python3

"""Script that takes in amino acid sequence as input and outputs
all possible DNA sequences that could encode this AA.
Usage: python3 Polk.py Any number of <AA sequence> Any number of <melting temps>"""

#List of melting temperatures
mts = []

#Make sure # of arguments is correct
import sys
if len(sys.argv) <= 2:
    sys.exit( __doc__)
for mt in sys.argv[2:]:
    mts.append(float(mt))

#Standard table of codons - a dictionary of single-letter
#amino acid code to a list of codon choices

aa_to_codons = {}
aa_to_codons[ "A" ] = ["GCA", "GCC", "GCG", "GCT" ]
aa_to_codons[ "C" ] = ["TGC", "TGT" ]
aa_to_codons[ "D" ] = ["GAC", "GAT" ]
aa_to_codons[ "E" ] = ["GAA", "GAG" ]
aa_to_codons[ "F" ] = ["TTC", "TTT" ]
aa_to_codons[ "G" ] = ["GGA", "GGC", "GGG", "GGT" ]
aa_to_codons[ "H" ] = ["CAC", "CAT" ]
aa_to_codons[ "I" ] = ["ATA", "ATC", "ATT" ]
aa_to_codons[ "K" ] = ["AAA", "AAG" ]
aa_to_codons[ "L" ] = ["CTA", "CTC", "CTG", "CTT", "TTA", "TTG" ]
aa_to_codons[ "M" ] = ["ATG" ]
aa_to_codons[ "N" ] = ["AAC", "AAT" ]
aa_to_codons[ "P" ] = ["CCA", "CCC", "CCG", "CCT" ]
aa_to_codons[ "Q" ] = ["CAA", "CAG" ]
aa_to_codons[ "R" ] = ["AGA", "AGG", "CGA", "CGC", "CGG", "CGT" ]
aa_to_codons[ "S" ] = ["AGC", "AGT", "TCA", "TCC", "TCG", "TCT" ]
aa_to_codons[ "T" ] = ["ACA", "ACC", "ACG", "ACT" ]
aa_to_codons[ "V" ] = ["GTA", "GTC", "GTG", "GTT" ]
aa_to_codons[ "W" ] = ["TGG" ]
aa_to_codons[ "Y" ] = ["TAC", "TAT" ]
aa_to_codons[ "*" ] = ["TAA", "TAG", "TGA" ]

def no_restriction_site(dna_string):
    "return false if restriction site present in dna string, else return true"
    restriction_sites = ["CATATG", "CTCGAG", "TCGA", "CTAG"]
    for site in restriction_sites:
        if site in dna_string:
            return False
    return True

def calc_mt(dna_string):
    "Calculate melting temperature of a DNA string"
    g_count = dna_string.count('G')
    c_count = dna_string.count('C')
    mt = 64.9 + (41.0 * (g_count + c_count - 16.4) / len(dna_string))
    return(mt)

def check_combinations(dna_string, aa_string):
    """Recursive function that takes an AA string and a DNA string as input.
    Converts the AA sequence into all possible DNA codon combinations"""
    # if this code is confusing to you, uncomment the print statement
    #print("Input DNA is:",dna_string,"Remaining AAs are:", aa_string, sep='\t')

    ####Return the DNA string if the AA string is empty, typically at the end
    if (len(aa_string)==0):
        if no_restriction_site(dna_string): #Check for restriction sites
            mt1 = calc_mt(dna_string) #Calculate melting temperature
            for mt in mts:
                if abs(mt - mt1) < 0.5: #Check if melting temperature within 0.5
                    print(dna_string + "\t" + str(mt1))
                    break

    #AA string is not empty, convert the Amino acids into respective DNA strings
    else:

        ###Get the first amino acid
        current_AA = aa_string[0];

        ####Loop through all the codons for this AA
        for single_codon in aa_to_codons[current_AA]:

            ####Create a dna string appended with the current codon for current AA
            new_dna_string = dna_string + single_codon

            ####Call the same function recursively with the generated string and rest of AA's
            check_combinations(new_dna_string,aa_string[1:])

# Main Script

print("Input parameters - ", sys.argv[1], mts, file = sys.stderr)
check_combinations( "", sys.argv[1] )
