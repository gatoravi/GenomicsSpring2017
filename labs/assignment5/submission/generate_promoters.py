import sys

def main():
    #Read gene annotation
    gene_annotations = sys.argv[1]
    with open(gene_annotations) as gafh:
        for line in gafh:
            line = line.rstrip("\n")
            chrom, start, end, gene, misc, strand = line.split("\t")
            if strand == "+":
                prom_start = int(start) - 1000
                prom_end = start
            else:
                prom_start = end
                prom_end = int(end) + 1000
            print("\t".join([chrom, str(prom_start), str(prom_end), gene, strand]))

main()
