import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def get_basename(name):
    return os.path.splitext(os.path.basename(name))[0]

def main():
    fig, ax = plt.subplots()
    histone_promoter = "H3K4me3_RPKM_promoter_CGI.bed"
    histone_nonpromoter = "H3K4me3_RPKM_non_promoter_CGI.bed"
    figname = get_basename(histone_promoter) + "_and_" + get_basename(histone_nonpromoter) + ".png"
    promoter_expression = []
    nonpromoter_expression = []
    with open(histone_promoter) as hp:
        for line in hp:
            line = line.rstrip("\n")
            fields = line.split("\t")
            rpkm = float(fields[-1])
            promoter_expression.append(rpkm)
    with open(histone_nonpromoter) as hnp:
        for line in hnp:
            line = line.rstrip("\n")
            fields = line.split("\t")
            rpkm = float(fields[-1])
            nonpromoter_expression.append(rpkm)
    ax.set_title('H3K4Me3 level at promoter/Non promoter CGIs')
    #ax.set_title('Distribution of CGI methylation levels')
    data = [promoter_expression, nonpromoter_expression]
    plt.boxplot(data, labels = ["promoter", "non-promoter"])
    plt.savefig(figname)


main()
