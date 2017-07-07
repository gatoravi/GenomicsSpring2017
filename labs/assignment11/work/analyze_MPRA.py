import sys
import math
import scipy.stats

"Analyze the MPRA counts"

def usage():
    "Usage"
    print("python3 analyze_MPRA.py pDNA_count.txt cDNA_count.txt")

pdna_counts = {} #Count for each barcode in pDNA
cdna_counts = {} #Count for each barcode in cDNA
barcode_ne = {} #Store the NE value for each barcode
variant_ref_barcodes = {} #For each variant store list of ref barcodes
variant_alt_barcodes = {} #For each variant store list of alt barcodes

def read_counts(dna, ds):
    "Read in the barcode-counts file"
    with open(dna) as dfh:
        #Remove newline at the end
        for line in dfh:
            line = line.rstrip("\n")
            #Split the fields
            fields = line.split("\t")
            #Figure out if REF/ALT
            allele = fields[-1]
            #get the variant id
            variant = fields[2]
            #Get the barcode and counts
            barcode, counts = fields[0:2]
            #Store the count for the barcode in the datastructure
            ds[barcode] = counts
            if allele == "REF":
                if variant not in variant_ref_barcodes:
                    variant_ref_barcodes[variant] = []
                variant_ref_barcodes[variant].append(barcode)
            elif allele == "ALT":
                if variant not in variant_alt_barcodes:
                    variant_alt_barcodes[variant] = []
                variant_alt_barcodes[variant].append(barcode)

def compute_ne():
    "Compute the NE value"
    for barcode in pdna_counts:
        if barcode in cdna_counts:
            #Compute normalized expression
            ne = math.log2(float(cdna_counts[barcode])/float(pdna_counts[barcode]))
            barcode_ne[barcode] = ne

def compute_average_ne():
    "Compute the average NE value for each variant"
    #Iterate through each variant
    for variant in variant_ref_barcodes:
        ref_ne = 0
        n_ref = 0
        alt_ne = 0
        n_alt = 0
        ref_nes = [] #Store all the nes for ref allele
        alt_nes = [] #Store all the nes for alt allele
        #Accumulate ref NEs for this variant
        for barcode in variant_ref_barcodes[variant]:
            ref_ne += barcode_ne[barcode]
            ref_nes.append(barcode_ne[barcode])
            n_ref += 1
        #Accumulate alt NEs for this variant
        for barcode in variant_alt_barcodes[variant]:
            alt_ne += barcode_ne[barcode]
            alt_nes.append(barcode_ne[barcode])
            n_alt += 1
        #Compute average ref NE
        average_ref_ne = ref_ne/n_ref
        #Compute average alt NE
        average_alt_ne = alt_ne/n_alt
        log2fc = average_alt_ne - average_ref_ne
        #Run MannWhitney U
        pvalue = scipy.stats.mannwhitneyu(alt_nes, ref_nes, alternative = "two-sided")[1]
        print(variant, log2fc, pvalue)

def main():
    "Everything starts here"
    #Check arguments
    if len(sys.argv) != 3:
        return usage()
    #PDNA file
    pdna = sys.argv[1]
    #CDNA file
    cdna = sys.argv[2]
    #Read in the counts into datastructures
    read_counts(pdna, pdna_counts)
    read_counts(cdna, cdna_counts)
    #Compute the NE values for each barcode
    compute_ne()
    #Compute the average NE values for each variant
    compute_average_ne()

#Call main
main()
