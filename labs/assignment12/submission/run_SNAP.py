"""
python3 run_SNAP.py alignments_directory output_directory 2>error_file
"""
import os
import subprocess
import sys

#Dictionary of genes and their dnds values
genes_dnds = {}

#Usage
def usage():
    print("python3 run_SNAP.py alignments_directory output_directory 2>error_file")

def process_dnds(output):
    "Process the dnds output file"
    #Get the gene-name
    gene = os.path.basename(output).replace(".fasta.dnds", "")
    with open(output) as dnds:
        #Go through the file
        for line in dnds:
            line = line.rstrip("\n")
            fields = line.split()
            #Get the dn/ds lines
            if len(fields) == 13:
                #Pick the right pair
                if fields[2] == "Scer" and fields[3] == "Spar":
                    #Ignore NA's and zeros
                    if fields[-1] != "NA":
                        if float(fields[-1]) != 0:
                            #store in the dictionary
                            genes_dnds[gene] = float(fields[-1])

def main():
    "Everything starts here"
    if len(sys.argv) < 3:
        return usage()
    #Get the alignments directory
    align_dir = sys.argv[1]
    #Get the output directory
    op_dir = sys.argv[2]
    #Get the list of alignments
    files = os.listdir(align_dir)
    #Iterate through each file and run SNAP.pl
    for file1 in files:
        ali = os.path.join(align_dir, file1)
        sys.stderr.write("Current file = " + ali + "\n")
        #Get the gene-name
        gene = os.path.basename(file1).replace(".fasta", "")
        sys.stderr.write("Gene:" + gene + "\n")
        sys.stderr.flush()
        #interpreter
        interpreter = "perl"
        #SNAP script
        snap = "./SNAP.pl"
        #Expected output
        output = os.path.join(op_dir, file1 + ".dnds")
        #List of params to subprocess
        params = [interpreter, snap, ali, op_dir]
        #Run SNAP.pl
        subprocess.call(params)
        #Check if output file exists
        if os.path.isfile(output):
            sys.stderr.write("Ran SNAP.pl succesfully!\n")
            #Process the output
            process_dnds(output)
        else:
            sys.stderr.write("Errored out!\n")
        sys.stderr.flush()
    #Write dnds to file
    dnds = os.path.dirname(align_dir) + "_all_dnds.txt"
    #Initialize sum to zero
    sum_dnds = 0
    with open(dnds, "w") as dnds_fh:
        #Haeder
        print("gene", "dnds", file = dnds_fh)
        #Iterate through all genes and their scores
        for gene, dnds in genes_dnds.items():
            #Write dnds to file
            if dnds > 1:
                print(gene, dnds)
            #Sum up to calculate average
            sum_dnds += dnds
            print(gene, dnds, file = dnds_fh)
    print("Average dnds(zeros and NAs removed) is ", sum_dnds/len(genes_dnds))

#Start
main()
