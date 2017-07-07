import sys

def usage():
    "usage"
    print("python3 compare_orf_callers.py mgm_output.faa all_orfs.faa")

#List of all the ORFS from MGM
mgm_orfs = []
#List of all my ORFs
my_orfs = []

def read_mgm_orfs(mgm):
    "Read MGM orfs"
    with open(mgm) as orf1:
        orf = ""
        for line in orf1:
            line = line.rstrip("\n")
            if line[0] != ">":
                orf += line
            else:
                if orf != "":
                    mgm_orfs.append(orf)
                    orf = ""
    mgm_orfs.append(orf)

def read_all_orfs(myorfs):
    "Read my orfs"
    with open(myorfs) as orf1:
        for line in orf1:
            line = line.rstrip("\n")
            if line[0] != ">":
                my_orfs.append(line)

def compare_orfs():
    "Compare MGM and my ORFs"
    matches = 0
    for orf in mgm_orfs:
        if orf in my_orfs:
            print("Match found ", orf)
            matches += 1
        else:
            print("Unique to MGM ", orf)
    print("Number of total MGM orfs", len(mgm_orfs))
    print("Number of total my orfs", len(my_orfs))
    mgm_unique = len(mgm_orfs) - matches
    my_unique = len(my_orfs) - matches
    print("Matches between MGM and my ORFs", matches)
    print("Unique to MGM ORFs", mgm_unique)
    print("Unique to my ORFs", my_unique)

def main():
    "Everything starts here"
    if len(sys.argv) < 3:
        return usage()
    read_mgm_orfs(sys.argv[1])
    read_all_orfs(sys.argv[2])
    compare_orfs()

main()
