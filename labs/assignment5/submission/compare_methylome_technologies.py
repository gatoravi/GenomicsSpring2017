import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

def get_basename(name):
    return os.path.splitext(os.path.basename(name))[0]

medip_meth = {}
mre_meth = {}
wgbs_meth = {}

def read_meth(file1, dict1):
    with open(file1) as mfh:
        for line in mfh:
            line = line.rstrip("\n")
            fields = line.split("\t")
            locus = fields[0] + ":" + fields[1] + ":" + fields[2]
            methylation = float(fields[-1])
            dict1[locus] = methylation

def plot_pairs_meth(dict1, dict2, imagename):
    list1 = []
    list2 = []
    for key1 in dict1:
        if key1 in dict2:
            list1.append(dict1[key1])
            list2.append(dict2[key1])
    print(imagename)
    print(len(list1), len(list2))
    print(scipy.stats.pearsonr(list1, list2)[0])
    fig, ax = plt.subplots()
    ax.scatter(list1, list2)
    plt.savefig(imagename)

def main():
    medip = sys.argv[1]
    mre = sys.argv[2]
    wgbs = sys.argv[3]
    medip_prefix = get_basename(medip)
    mre_prefix = get_basename(mre)
    wgbs_prefix = get_basename(wgbs)
    print(medip_prefix, mre_prefix, wgbs_prefix)
    read_meth(medip, medip_meth)
    read_meth(mre, mre_meth)
    read_meth(wgbs, wgbs_meth)
    print(len(medip_meth), len(mre_meth), len(wgbs_meth))
    medip_vs_mre = medip_prefix + "_vs_" + mre_prefix + ".png"
    medip_vs_wgbs = medip_prefix + "_vs_" + wgbs_prefix + ".png"
    mre_vs_wgbs = mre_prefix + "_vs_" + wgbs_prefix + ".png"
    plot_pairs_meth(medip_meth, mre_meth, medip_vs_mre)
    plot_pairs_meth(medip_meth, wgbs_meth, medip_vs_wgbs)
    plot_pairs_meth(mre_meth, wgbs_meth, mre_vs_wgbs)

main()
