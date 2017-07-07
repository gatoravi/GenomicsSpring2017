import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

"Quantify hets, homs for SNVs and INDELs"

#Usage: python3 quantify_genotype.py SNV_indel.biallelic.vcf
#Get the SNV indel file
snv_indel = sys.argv[1]
#Counts of various classes
snv_count = 0
indel_count = 0
snv_hom_ref = 0
snv_het = 0
snv_hom_alt = 0
snv_missing = 0
indel_hom_ref = 0
indel_het = 0
indel_hom_alt = 0
indel_missing = 0

def count_snvs_indels():
    "Read in SNV and INDELs"
    global snv_count, indel_count
    global snv_hom_ref, snv_het, snv_hom_alt, snv_missing
    global indel_hom_ref, indel_het, indel_hom_alt, indel_missing
    with open(snv_indel) as sifh:
        for line in sifh:
            line = line.rstrip("\n")
            fields = line.split("\t")
            #Skip header
            if line[0] != "#":
                na12878 = fields[10]
                if len(fields[3]) == 1 and len(fields[4]) == 1: #SNVS
                    #print("snv", line)
                    snv_count += 1
                    #hom-ref
                    if "0/0" in na12878:
                        snv_hom_ref += 1
                    #het
                    elif "0/1" in na12878:
                        snv_het += 1
                    #hom-alt
                    elif "1/1" in na12878:
                        snv_hom_alt += 1
                    #missing
                    elif "./." in na12878:
                        snv_missing += 1
                        snv_count -= 1
                else:
                    #print("indel", line)
                    indel_count += 1
                    #hom-ref
                    if "0/0" in na12878:
                        indel_hom_ref += 1
                    #het
                    elif "0/1" in na12878:
                        indel_het += 1
                    #hom-alt
                    elif "1/1" in na12878:
                        indel_hom_alt += 1
                    #missing
                    elif "./." in na12878:
                        indel_missing += 1
                        indel_count -= 1


count_snvs_indels() #Counting happens here
#pRint SNV counts
print("snv_count", snv_count)
print("snv_hom_ref", snv_hom_ref)
print("snv_het", snv_het)
print("snv_hom_alt", snv_hom_alt)
print("snv_missing", snv_missing)
print("snv_total", snv_hom_ref + snv_het + snv_hom_alt + snv_missing)

#compute HWE expectation
n = (snv_hom_ref + snv_het + snv_hom_alt)
p = (2 * snv_hom_ref + snv_het)/(2*n)
q = 1 - p
print("Expectation under HWE ", p * p * n, 2 * p * q * n, q * q * n)

#Print indel counts
print("indel_count", indel_count)
print("indel_hom_ref", indel_hom_ref)
print("indel_het", indel_het)
print("indel_hom_alt", indel_hom_alt)
print("indel_missing", indel_missing)
print("indel_total", indel_hom_ref + indel_het + indel_hom_alt + indel_missing)

#compute HWE expectation for indels
n = (indel_hom_ref + indel_het + indel_hom_alt)
p = (2 * indel_hom_ref + indel_het)/(2*n)
q = 1 - p
print(p, q)
print("Expectation under HWE ", p * p * n, 2 * p * q * n, q * q * n, p * p * n + 2 * p * q * n +  q * q * n)

