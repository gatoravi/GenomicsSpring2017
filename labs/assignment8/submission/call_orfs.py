import sys

#Variable to keep track of ORF number
orf_number = 0
fna_fh = open("all_orfs.fna", "w")
faa_fh = open("all_proteins.faa", "w")

#The table was borrowed from https://www.biostars.org/p/2903/
rna_to_aa_map = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def usage():
    "Usage"
    print("Usage: python3 call_orfs.py contigs.fna")

def print_orf(orf1):
    "Print the orf"
    global orf_number
    orf_number += 1
    print(">orf" + str(orf_number), file = fna_fh)
    print(orf1, file = fna_fh)

def print_orf_aa(orf1):
    "Print the translated orf"
    global orf_number
    print(">orf" + str(orf_number), file = faa_fh)
    orf_translated = ""
    orf1 = orf1.replace("T", "U")
    for i in range(0, len(orf1) - 2, 3):
        codon = orf1[i:i+3]
        aa = rna_to_aa_map[codon]
        #Append
        orf_translated += aa
    print(orf_translated, file = faa_fh)

def call_orf1(seq):
    "Call orf from one sequence"
    #Empty ORF to start with
    orf1 = ""
    start = stop = False
    for i in range(0, len(seq) - 2, 3):
        if i <= len(seq) - 3:
            codon = seq[i:i+3]
        #print("At", codon, orf1, start, stop)
        if start:
            if codon in ["TAA", "TGA", "TAG"]: #Stop codons
                stop = True
            else:
                orf1 += codon
        #Initiating condition
        elif codon == "ATG":
            start = True
            orf1 = codon
        #Terminating condition
        if start and stop:
            start = stop = False
            #Check length of ORF
            if len(orf1) > 100:
                print_orf(orf1)
                print_orf_aa(orf1)
            orf1 = ""

def reversecomp(seq):
    "Get the reverse complement"
    rc = ""
    revcomp_dict = { 'A' : 'T', 'G' : 'C', 'C' : 'G', 'T' : 'A' }
    for nuc in seq:
        rc += revcomp_dict[nuc]
    return rc[::-1] #reverse

def call_orfs(fasta):
    "Iterate through fasta"
    with open(fasta) as fastafh:
        for line in fastafh:
            line = line.rstrip("\n")
            if line[0] != ">":
                call_orf1(line)
                call_orf1(line[1:])
                call_orf1(line[2:])
                #Repeat for reverse complement
                rc = reversecomp(line)
                call_orf1(rc)
                call_orf1(rc[1:])
                call_orf1(rc[2:])

def main():
    "Everything starts here"
    if len(sys.argv) < 2:
        return usage()
    call_orfs(sys.argv[1])
    fna_fh.close()
    faa_fh.close()

main()
