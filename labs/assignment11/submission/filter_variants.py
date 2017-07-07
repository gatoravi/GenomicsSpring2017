import sys

"""
  python3 filter_variants.py variant_to_barcode.txt  > filtered_variant_to_barcode.txt
  This script filters out variants with fewer than or equal to six barcodes for either allele"
"""

def main():
    "Everything starts here"
    #Open the variant readcount file
    with open(sys.argv[1]) as fh:
        header = True #Skip header
        #Iterate through the lines
        for line in fh:
            line = line.rstrip("\n")
            #Skip header
            if header:
                print(line)
                header = False
                next
            #Split the fields
            fields = line.split("\t")
            #ref barcode
            ref_barcodes = fields[1].split(":")
            #alt barcode
            alt_barcodes = fields[2].split(":")
            #Filter out
            if(len(alt_barcodes) > 6 and len(ref_barcodes) > 6):
                print(line)


#Call the main function
main()
