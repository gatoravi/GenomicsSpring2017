"""
Plot gene length vs dn_ds
python3 plot_gene_length_vs_dnds.py <run_SNAP.py error file> <run_SNAP.py output file of dnds values>
"""

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Store the length of each gene
genes_lengths = {}
#List of dnds values
dndses = []
#List of gene lengths
lengths = []

#Usage
def usage():
    print("python3 plot_gene_length_vs_dnds.py <run_SNAP.py error file> <run_SNAP.py output file of dnds values>")

#Get the gene lengths
def parse_err_file(err_file):
    "Parse the error file"
    with open(err_file) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if "Gene:" in line:
                gene = line.replace("Gene:", "")
            elif "Sequence Length: " in line:
                length = int(line.replace("Sequence Length: ", ""))
                genes_lengths[gene] = length

#Get the lengths vs dnds
def parse_dnds(dnds_file):
    "Read the dnds file"
    #Skip header
    header = True
    #Iterate through dnds
    with open(dnds_file) as dnds:
        for line in dnds:
            line = line.rstrip("\n")
            #Skip header
            if header:
                header = False
                next
            else:
                #Get the gene and the dnds score
                fields = line.split()
                gene = fields[0]
                dnds = float(fields[1])
                #Check for length
                length = genes_lengths[gene]
                dndses.append(dnds)
                lengths.append(length)

#plot dnds vs length
def plot_dnds_length():
    plt.xlim([0, 0.5])
    plt.scatter(dndses, lengths)
    plt.savefig("gene_length_vs_dnds.png")

#Start
def main():
    "Everything starts here"
    if len(sys.argv) != 3:
        return usage()
    #Get the error file
    err_file = sys.argv[1]
    #Get the otuput file
    genes_dnds = sys.argv[2]
    #Parse the error file and get lengths
    parse_err_file(err_file)
    #pArse the dnds file
    parse_dnds(genes_dnds)
    #Plot dnds vs length
    plot_dnds_length()

main()
