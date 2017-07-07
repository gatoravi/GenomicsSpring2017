Please provide the exact command line arguments you used to generate your results.
python nuc_count.py hs_ref_GRCh38.p7_chr20.fa
python3 make_seq.py 1000000 0.28 0.22 0.22 0.28 > random_seq_1M.txt
-
Question 1:
Raw Counts
('A: ', 17983955)
('C: ', 14046812)
('G: ', 14223634)
('T: ', 18179110)
('N: ', 97761)
-
Question 2:
Frequencies
('A: ', 0.27910872340946935)
('C: ', 0.21800475842454092)
('G: ', 0.22074901366154018)
('T: ', 0.2821375045044496)
-
Question 3:
Dinucleotide Frequencies - human chr20
AA : 0.09
AC : 0.05
AG : 0.07
AT : 0.07
CA : 0.07
CC : 0.06
CG : 0.01
CT : 0.07
GA : 0.06
GC : 0.05
GG : 0.06
GT : 0.05
TA : 0.06
TC : 0.06
TG : 0.08
TT : 0.09
-
Dinucleotide Frequencies - simulated data
AA : 0.08
AC : 0.06
AG : 0.06
AT : 0.08
CA : 0.06
CC : 0.05
CG : 0.05
CT : 0.06
GA : 0.06
GC : 0.05
GG : 0.05
GT : 0.06
TA : 0.08
TC : 0.06
TG : 0.06
TT : 0.08
-
Compare the two lists of frequencies. What are the differences? Can you provide a biological explanation for these differences?:
CG in the chr20 dataset has a frequency of 0.01, whereas in the
simulated dataset I see a frequency of 0.05. This depletion of CGs
is due to the spontaneous deamination of methylated Cs to Ts in CpGs.
There also appears to be a slight enrichment in TG 0.08 vs 0.06 which
could be due to the same phenomenon.

TA has a frequency of 0.06 in the chr20 dataset whereas in the simulated
data it has a frequency of 0.08, I'm not sure why this might be, this
could be due to chance.

-
Comments:
{}
-
Suggestions:
{}
-

