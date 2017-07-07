import sys
import os.path
"Count number of barcodes in reads"

def usage():
    "Usage"
    print("python3 count_barcodes.py <raw reads fastq> filtered_variant_to_barcode.txt")

#Dictionary with ref barcodes for each variant
#Key is variant-id, value is list of ref barcodes
variant_barcodes_ref = {}
#Dictionary with alt barcodes for each variant
#Key is variant-id, value is list of alt barcodes
variant_barcodes_alt = {}
#Counts for each barcode
barcode_counts = {}

def read_variant_to_barcode(variant_to_barcode):
    "Read the barcodes for each variant"
    with open(variant_to_barcode) as vtbfh:
        for line in  vtbfh:
            #Remove newline at the end
            line = line.rstrip("\n")
            #Split the fields
            fields = line.split("\t")
            #Get the variant ID
            variant = fields[0]
            #ref barcode
            ref_barcodes = fields[1].split(":")
            #alt barcode
            alt_barcodes = fields[2].split(":")
            #Store the barcodes for ref, alt
            variant_barcodes_ref[variant] = ref_barcodes
            variant_barcodes_alt[variant] = alt_barcodes

def parse_fastq(fq1):
    "Parse the FASTQ file"
    #Read through fasta file
    with open(fq1) as ffh:
        #Track line numbers
        linenum = 0
        for line in ffh:
            linenum += 1
            line = line.rstrip("\n")
            #Only look at the sequence line
            if linenum % 2 == 0 and linenum % 4 != 0:
                #Get the barcode
                barcode = line[14:23]
                #Check if barcode seen before
                if barcode not in barcode_counts:
                    barcode_counts[barcode] = 0
                #Increment count for barcode
                barcode_counts[barcode] += 1

def print_output(opfile):
    "Match barcodes to variants and print counts"
    filtered_reads = 0
    with open(opfile, "w") as ofh:
        #Iterate through the barcodes
        for barcode in barcode_counts:
            ref = "NA"
            variant1 = "NA"
            for variant in variant_barcodes_ref:
                #Check if barcode matches any in the filtered set
                if barcode in variant_barcodes_ref[variant]:
                    #Set ref/alt
                    ref = "REF"
                    variant1 = variant
            #Check if not ref
            if ref == "NA":
                for variant in variant_barcodes_alt:
                    #Check if barcode matches any in the filtered set
                    if barcode in variant_barcodes_alt[variant]:
                        #Set ref/alt
                        ref = "ALT"
                        variant1 = variant
            if ref != "NA": #Found variant with this barcode
                #Print barcodes that are not filtered out
                print(barcode, barcode_counts[barcode], variant1, ref, sep = "\t", file = ofh)
            else:
                #accumulate number of filtered out reads
                filtered_reads += barcode_counts[barcode]
    print("Number of reads filtered out is: ", filtered_reads, file = sys.stderr)

def main():
    "Everything starts here"
    if len(sys.argv) < 3:
        return usage()
    #Parse command line arguments
    fastq = sys.argv[1]
    variant_to_barcode = sys.argv[2]
    #file to write the output to
    opfile = fastq.replace(".fq", "") + "_count.txt"
    print("Output file:", opfile)
    #Read the barcodes into datastructures
    read_variant_to_barcode(variant_to_barcode)
    #Parse the fastq file
    parse_fastq(fastq)
    #Print the output
    print_output(opfile)

main()
