import sys

blast_op = sys.argv[1]
with open(blast_op) as bfh:
    for line in bfh:
        line = line.rstrip("\n")
        fields = line.split("\t")
        percent_identity = fields[2]
        length = float(fields[3])
        slen = float(fields[-2])
        if length/slen > 0.85:
            print(line)
