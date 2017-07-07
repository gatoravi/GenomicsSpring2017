import sys

#Get the resfams output
resfams = sys.argv[1]

#List of genes
genes = {}

with open(resfams) as rfh:
    for line in rfh:
        line = line.rstrip("\n")
        if line[0] != "#": #Ignore headers
            fields = line.split()
            gene = fields[1]
            genes[gene] = 1
print("number of unique genes: ", len(genes))
