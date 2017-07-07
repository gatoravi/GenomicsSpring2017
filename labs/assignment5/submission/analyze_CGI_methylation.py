import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    cgi_methylation = sys.argv[1]
    fig_name = sys.argv[2]
    methylation_column = int(sys.argv[3])
    cgi_meths = []
    with open(cgi_methylation) as cmh:
        for line in cmh:
            line = line.rstrip("\n")
            fields = line.split("\t")
            cgi_meths.append(float(fields[methylation_column]))
    fig, ax = plt.subplots()
    ax.set_xlabel('Methylation level at CGIs')
    ax.set_title('Distribution of CGI methylation levels')
    plt.hist(cgi_meths)
    plt.savefig(fig_name)

main()
