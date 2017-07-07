#!/usr/bin/env python3
#rsears 2/3/15 
""" 
This script counts nucleotides in a fq file

Usage: python3 nuc_count.py <fastQfile>
""" 

# import sys module
import sys

#Check if an argument was passed to the python script
#If not exit exit and print the documentation

if (len(sys.argv)!=2):
	sys.exit(__doc__) 

#Assign variable to Fastq file
fastQ=sys.argv[1]

#Initalize a nucleotide string
nucleotides=[]

#open the file,and skip the first line
count=0
with open(fastQ) as f:
    next(f)
    for line in f:
        count=count+1
        if count%4==1: #Every 4th line is now the sequence we want
            #Append to a list so every element is a read (do not concatenate)
            nucleotides.append(line.rstrip().upper())
#            print(nucleotides)

#Create nucleotide and dinucleotide dictionaries
ACTG="ACTG"

nuc_dict={}
dinuc_dict={}

for i in range(0,len(ACTG)):
     my_nuc=ACTG[i] 
     nuc_dict[my_nuc]=0
   
     for j in range(0,len(ACTG)):
         my_dinuc=ACTG[i]+ACTG[j]
         dinuc_dict[my_dinuc]=0

#Count nucleotides within each read and add to ongoing sum
for i in range(0,len(nucleotides)):
    for j in range(0,len(ACTG)):
        nuc_dict[ACTG[j]]=nuc_dict[ACTG[j]]+nucleotides[i].count(ACTG[j])
print ("\nRaw Counts")
print ("A:",nuc_dict['A'],"\nC:",nuc_dict['C'],"\nG:",nuc_dict['G'],"\nT:",nuc_dict['T'])

#Calculate and print nucleotide frequencies 
As=nuc_dict['A']
Cs=nuc_dict['C']
Gs=nuc_dict['G']
Ts=nuc_dict['T']
bottom=As+Cs+Gs+Ts 
afreq = As/bottom
cfreq = Cs/bottom
gfreq = Gs/bottom
tfreq = Ts/bottom
expected_afreq = 0.27910872340946935
expected_cfreq = 0.21800475842454092
expected_gfreq = 0.22074901366154018
expected_tfreq = 0.2821375045044496

print ("\nNucleotide Frequencies")
print ("A:",As/bottom,"\nC:",Cs/bottom,"\nG:",Gs/bottom,"\nT:",Ts/bottom)
print ("\nNucleotide Enrichment")
print ("A:",afreq/0.25,"\nC:", cfreq/0.25,"\nG:", gfreq/0.25,"\nT:", tfreq/0.25)
print ("A:",afreq/expected_afreq,"\nC:", cfreq/expected_cfreq,"\nG:", gfreq/expected_gfreq,"\nT:", tfreq/expected_tfreq)

nucfreq = {}
nucfreq['A'] = afreq
nucfreq['C'] = cfreq
nucfreq['G'] = gfreq
nucfreq['T'] = tfreq
expected_dinuc_freq = {}
expected_dinuc_freq['AA'] = 0.09
expected_dinuc_freq['AC'] = 0.05
expected_dinuc_freq['AG'] = 0.07
expected_dinuc_freq['AT'] = 0.07
expected_dinuc_freq['CA'] = 0.07
expected_dinuc_freq['CC'] = 0.06
expected_dinuc_freq['CG'] = 0.01
expected_dinuc_freq['CT'] = 0.07
expected_dinuc_freq['GA'] = 0.06
expected_dinuc_freq['GC'] = 0.05
expected_dinuc_freq['GG'] = 0.06
expected_dinuc_freq['GT'] = 0.05
expected_dinuc_freq['TA'] = 0.06
expected_dinuc_freq['TC'] = 0.06
expected_dinuc_freq['TG'] = 0.08
expected_dinuc_freq['TT'] = 0.09

#Store expected dinuc counts:
'''
for nuc1 in "ACGT":
    for nuc2 in "ACGT":
        dinuc = nuc1 + nuc2
        expected_dinuc_freq[dinuc] = nucfreq[nuc1] * nucfreq[nuc2]
'''

#Use an overlapping count to count dinucleotides
for i in range(0,len(nucleotides)): #Go through entire list
     for j in range(0,len(nucleotides[i])-1): #Go through length of string -1
         this_dinucleotide=(nucleotides[i])[j]+(nucleotides[i])[j+1] #get dinucleotide
         if this_dinucleotide in dinuc_dict.keys(): #if nucleotide exists
             dinuc_dict[this_dinucleotide]=dinuc_dict[this_dinucleotide]+1 #add to ongoing sum

#Loop through the keys in the dictionary using the sorted command.

#Print the counts
print ("\nDinucleotide Count")
for all_dinuc in sorted(dinuc_dict.keys()):
        print (all_dinuc+":"+str(dinuc_dict[all_dinuc]))

#Print the frequencies
denom=sum(dinuc_dict.values()) 
print ("\nDinucleotide Frequencies")
for all_dinuc in sorted(dinuc_dict):
    print (all_dinuc+":"+str(float(dinuc_dict[all_dinuc])/denom))

#Print the enrichment
print ("\nDinucleotide Enrichment")
for all_dinuc in sorted(dinuc_dict):
    expected_freq = expected_dinuc_freq[all_dinuc]
    observed_freq = float(dinuc_dict[all_dinuc])/denom
    print(all_dinuc+":"+str(observed_freq/expected_freq))

