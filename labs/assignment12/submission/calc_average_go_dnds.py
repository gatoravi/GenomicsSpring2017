"""
python3 calc_average_go_dnds.py <gff> <run_SNAP.py output file of dnds values>
"""

import sys

#Usage
def usage():
    print("python3 calc_average_go_dnds.py <gff> <run_SNAP.py output file of dnds values>")

#Store list of genes for each GO term
go_genes = {}

#Store the dnds for each gene
genes_dnds = {}

#Summarize and print output
def summarize_output():
    "Summarize the output"
    for go, genes in go_genes.items():
        total_dnds = 0
        for gene in genes:
            total_dnds += genes_dnds[gene]
        #Compute average
        average_dnds = total_dnds/len(genes) 
        print(go, average_dnds, ",".join(genes), sep = "\t")

#Parse the GFF file
def parse_gff(gff1):
    "Parse the GFF file"
    with open(gff1) as gfh:
        for line in gfh:
            line = line.rstrip("\n")
            fields = line.split("\t")
            if len(fields) > 2 and fields[2] == "gene":
                infos = fields[8].split(";")
                for info in infos:
                    #Get teh gene name
                    if "Name=" in info:
                        gene = info.replace("Name=", "")
                        if gene not in genes_dnds:
                            break
                    if "Ontology_term=" in info:
                        #Get teh gene ontologies
                        gos = info.replace("Ontology_term=", "")
                        gos_split = gos.split(",")
                        for go in gos_split:
                            if go not in go_genes:
                                go_genes[go] = []
                            #Append gene to this go list
                            go_genes[go].append(gene)

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
                genes_dnds[gene] = dnds
def main():
    "Everything starts here"
    if len(sys.argv) != 3:
        return usage()
    #Get the gff
    gff = sys.argv[1]
    #Get the otuput file
    dnds = sys.argv[2]
    #pArse the dnds file
    parse_dnds(dnds)
    #Parse the GFF file
    parse_gff(gff)
    #Summarize and print output
    summarize_output()

main()
