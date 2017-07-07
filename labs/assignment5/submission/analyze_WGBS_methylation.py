import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    methylation_counts = sys.argv[1]
    prefix = os.path.splitext(os.path.basename(methylation_counts))[0]
    output_meth = prefix + "_CpG_methylation.bed"
    methylation_dist_png = prefix + "_methylation_distribution.png"
    cpg_dist_png = prefix + "_CpG_coverage_distribution.png"
    print("Analyzing methylation file, ", methylation_counts)
    zerocoverage = 0
    cpgcount = 0
    cpg_coverages = []
    methylation_levels = []
    with open(methylation_counts) as mcfh:
        omh = open(output_meth, "w")
        for line in mcfh:
            cpgcount += 1
            chrom, start, end, c_count, t_count = line.split("\t")
            c_count = int(c_count)
            t_count = int(t_count)
            coverage = c_count + t_count
            if coverage >= 0 and coverage <= 100:
                cpg_coverages.append(coverage)
            if coverage != 0:
                methylation_level = c_count/(c_count + t_count)
                methylation_levels.append(methylation_level)
                print("\t".join([chrom, str(start), str(end), str(methylation_level)]), file = omh)
            else:
                zerocoverage += 1
    print("Fraction of zero CpGs is ", zerocoverage/cpgcount)
    print("Mean CpG coverage is ", np.mean(cpg_coverages))
    fig, ax = plt.subplots()
    ax.set_xlabel('Methylation level')
    ax.set_title('Distribution of CpG methylation levels')
    plt.hist(methylation_levels)
    plt.savefig(methylation_dist_png)
    fig, ax = plt.subplots()
    ax.set_xlabel('CpG coverage')
    ax.set_title('Distribution of CpG coverage(between zero and hundred)')
    plt.hist(cpg_coverages)
    plt.savefig(cpg_dist_png)

main()
