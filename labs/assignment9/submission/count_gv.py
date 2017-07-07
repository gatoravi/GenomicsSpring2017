import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

"This script counts genetic variation from SNV-indel and SV files"

#Usage: python3 count_gv.py SNV_indel.biallelic.vcf sv.reclassed.filtered.vcf
#Get the SNV indel file
snv_indel = sys.argv[1]

#Get the SV file
sv = sys.argv[2]

snv_count = 0 #count number of snvs
indel_count = 0 #count number of indels
bnd_count = 0 # BNDs
del_count = 0 # large dels
mei_count = 0 # MEIs
dup_count = 0 #tandem dups
inv_count = 0 #inversion

#Lengths of variants
mei_lens = []
del_lens = []
indel_lens = []

#Function where counting of SNVs, INDELs happens
def count_snvs_indels():
    "Read in SNV and INDELs"
    global snv_count, indel_count
    #Read in file
    with open(snv_indel) as sifh:
        for line in sifh:
            line = line.rstrip("\n")
            fields = line.split("\t")
            if line[0] != "#":
                na12878 = fields[10]
                #Check for hom and missing genotypes
                if "0/0" not in na12878 and "./." not in na12878:
                    #SNV
                    if len(fields[3]) == 1 and len(fields[4]) == 1:
                        #print("snv", line)
                        snv_count += 1
                    #INDEL
                    else:
                        #print("indel", line)
                        indel_count += 1
                        indel_lens.append(abs(len(fields[3]) - len(fields[4])))

#Counting of SVs happens here
def count_svs():
    "Read in SVs"
    global bnd_count
    global mei_count
    global del_count
    global dup_count
    global inv_count
    global mei_lens, del_lens
    with open(sv) as svfh:
        for line in svfh:
            line = line.rstrip("\n")
            fields = line.split("\t")
            #Ignore header
            if line[0] != "#":
                na12878 = fields[10]
                #Ignore homs and missing
                if "0/0" not in na12878 and "./." not in na12878:
                    info =  fields[7]
                    info_fields = info.split(";")
                    for field in info_fields:
                        #Get the length
                        if "SVLEN" in field:
                            svlen = abs(int(field.replace("SVLEN=", "")))
                            break
                    #BND
                    if "SVTYPE=BND" in info:
                        bnd_count += 1
                    #MEI
                    elif "SVTYPE=MEI" in info:
                        mei_count += 1
                        mei_lens.append(svlen)
                    #DEL
                    elif "SVTYPE=DEL" in info:
                        del_count += 1
                        del_lens.append(svlen)
                    #DUP
                    elif "SVTYPE=DUP" in info:
                        dup_count += 1
                    #INV
                    elif "SVTYPE=INV" in info:
                        inv_count += 1

#plot the histograms
def print_len_histogram(lengths, title):
    fig, ax = plt.subplots()
    #Plot the deletions on a log scale
    if title == "histogram_deletions":
        lengths = np.log10(lengths)
        plt.xlabel("log10(lengths)")
    else:
        plt.xlabel("Length")
    #Histogram
    ax.hist(lengths, bins = 100)
    plt.title(title)
    fig.savefig(title + ".png", dpi=250)

#Start counting
count_snvs_indels()
#Count SVs
count_svs()

#accumulate counts
total_gv = snv_count + indel_count + bnd_count + del_count + dup_count + mei_count + inv_count
sv_count = bnd_count + del_count + dup_count + mei_count + inv_count
#output the counts
print("snv_count", snv_count)
print("indel_count", indel_count)
print("bnd_count", bnd_count)
print("del_count", del_count)
print("dup_count", dup_count)
print("mei_count", mei_count)
print("inv_count", inv_count)
print("total genetic variants", total_gv)
print("sv count", sv_count)
print("prop_sv ", sv_count/total_gv)

#plot the lengths
print_len_histogram(indel_lens, "histogram_indels")
print_len_histogram(del_lens, "histogram_deletions")
print_len_histogram(mei_lens, "histogram_meis")
