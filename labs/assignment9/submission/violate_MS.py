import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

"Identify violations of Mendelian segregation"
#Usage: python3 violate_MS.py  SNV_indel.biallelic.vcf 20
#Get the SNV indel file
snv_indel = sys.argv[1]
#GQ threshold
threshold = int(sys.argv[2])

def count_snvs_indels():
    "Read in SNV and INDELs"
    global snv_count, indel_count
    global snv_hom_ref, snv_het, snv_hom_alt, snv_missing
    global indel_hom_ref, indel_het, indel_hom_alt, indel_missing
    with open(snv_indel) as sifh:
        for line in sifh:
            line = line.rstrip("\n")
            fields = line.split("\t")
            #Ignore headers
            if line[0] != "#":
                #Get the genotypes
                na12878_gt = fields[10].split(":")[0]
                na12891_gt = fields[-3].split(":")[0]
                na12892_gt = fields[-2].split(":")[0]
                #Ignore missing
                if na12878_gt != "./." and na12891_gt != "./." and na12892_gt != "./.":
                    #Get the genotype quality
                    na12878_gq = int(fields[10].split(":")[3])
                    na12891_gq = int(fields[-3].split(":")[3])
                    na12892_gq = int(fields[-2].split(":")[3])
                    #check genotype quality threshold
                    if na12878_gq > threshold and na12891_gq > threshold and na12892_gq > threshold:
                        #Check for mendelian incompatibility
                        if na12878_gt[0] not in na12891_gt or na12878_gt[1] not in na12892_gt:
                            if na12878_gt[1] not in na12891_gt or na12878_gt[0] not in na12892_gt:
                                print(na12878_gt, na12891_gt, na12892_gt)

count_snvs_indels()
