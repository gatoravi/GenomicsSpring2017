USAGE:
{Please provide the exact command line arguments you used to run map_sequence_starter.py and generate your results}
python3 map_sequence_starter.py  scott_mouse_cDNAs.fa mckinley_raw_reads.txt
-
Question 1:
{Output from running map_sequence_starter.py on the Scott cDNAs and McKinley sequencing reads}
Read in the cDNAs
Created dictionary
Name    Reads   Reads per BP
Abcg2   7       0.0035460992907801418
Atp1A1  370     0.12044270833333333
Cd34    7       0.006092254134029591
ChAT    0       0.0
Gap43   36      0.05263157894736842
Gfap    38      0.029389017788089715
Mbp     304     0.4037184594953519
Myod1   0       0.0
Olig2   6       0.006172839506172839
Tubb3   154     0.11382113821138211
{Question 1.2 Genes highly expressed, their function, and why?}
Mbp, Tubb3 and Atp1A1 are highly expressed.
Mbp is needed for myelin production in Schwann cells and
oligodendrocytes.
Tubb3 produces beta tubulins needed for making microtubules in
neurons.
Atp1A1 produces membrane proteins necessary for electrical excitibility
of nerves and muscles.
These genes all indicate function in neuronal cell types, this could
indicate the type of tissue the RNA was extracted from.

{Question 1.3 Genes lowly or not expressed, their function, and why?}
ChAT, Myod1, Abcg2 and Olig2
Abcg2 transports various molecules across membranes.
ChAT is responsible for the synthesis of the neurotransmitter
acetylcholine.
Myod1 is a protein that plays a major role in muscle differentiation.
Olig2 is a basic helix-loop-helix transcription factor.

These genes are probably not expressed in the tissue that the RNA sample
is from.

-
Question 2:
Yes there is an enrichment.
{Statistical test used and explanation}
I used a Fisher's exact test to compare the proportions. The null
hypothesis is 30/300 and 10/20 are not statistically different, the
alternative hypothesis is that 10/20 is greater than 30/300.
{one-tailed or two-tailed}
I used a one-tailed fisher's exact test, the alternative
hypothesis being greater.
> fisher.test(matrix(c(270, 30, 10, 10), nrow = 2),
alternative="greater")

           Fisher's Exact Test for Count Data

           data:  matrix(c(270, 30, 10, 10), nrow = 2)
           p-value = 2.295e-05
           alternative hypothesis: true odds ratio is greater than 1
           95 percent confidence interval:
            3.568798      Inf
            sample estimates:
            odds ratio
              8.888141
{p-value}
2.295e-05

An alternative test to use could be a chi-squared test.
-
Question 3:
If we didn't normalize by the length of the gene, larger genes would
have larger counts since the RNA transcripts from these genes are
larger and hence more kmers. Normalizing helps compare across genes.
-
Question 4:
I would create an index for the transcriptome like a Burrows wheeler
index and map the reads against this index. The mapping would be faster
and take less space in memory.

{Limitation 1}
As the size of the hash table gets really large with more kmers the hash
table will get slower.
{Limitation 2}
We need to account for kmers that are present in more than one gene.
These might not be counted or shared equally amongst all the genes that
have this kmer.
{Limitation 3}
Alternate spliced transcripts could be missed by just considering one
isoform per gene.
-
Comments:
{Things that went wrong or you can not figure out}
-
Suggestions:
{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}

