Part I

Question 1:
{Exact command to run count_gv.py}
python3 count_gv.py SNV_indel.biallelic.vcf sv.reclassed.filtered.vcf
{Output count table}
snv_count 4021968
indel_count 474608
bnd_count 5296
del_count 1662
dup_count 523
mei_count 1200
inv_count 95
total genetic variants 4505352
sv count 8776
prop_sv  0.0019479055132651123
-
Question 2:
{Proportion of  genomic variants are SVs}
0.002 or 0.2%
-
Question 3:
{Describe the spectrum of SVs for the individual NA12878}
Most of the variants observed are single nucleotide polymorphisms.
The indel mutation rate is an order lower than the SNPs.
For SV's the most common event are deletions followed by mobile
element insertions. These are followed by fewer duplications and
much fewer inversions. There might be an ascertainment bias involved
in interpreting these results since some classes of SVs are harder
to detect with short read sequencing technology.
-
Question 4:
{Place the three histograms in your submission directory}
Done!
{Describe the distributions observed in each of the histograms}
Most of the indels are very small, smaller than ten basepairs. The
number of indels decreases with length.
The deletion distribution follows a much wider range and hence I have
plotted the x-axis on a log scale. There appears to be a lot of
deletions around 500 basepairs in length. There is a heavy tail in
the distribution indication some deletions with very large sizes around
100,000 b.p or so.
The MEI length distribution is a mixture of different classes of
inserted elements such as Alu(around 300 b.p), L1 (around 6kb),
and SVA elements.
{Speculate how the length distribution might differ if we limit the data to exonic indels?}
If we limit to exonic indels we will see spikes in indels of size
multiples of 3, for example 3,6,9. This is because these indels will
retain the coding frame and are perhaps comparitively less harmful
than frameshift indels.
-
Part II

Question 5:
{Exact command to run quantify_genotype.py}
python3 quantify_genotype.py SNV_indel.biallelic.vcf
{Output count table}
snv_hom_ref 3017287
snv_het 2555710
snv_hom_alt 1466258
snv_missing 71817
snv_total 7111072
Expectation under HWE  2620766.657858538 3348750.6842829245 1069737.6578585373
indel_hom_ref 452756
indel_het 302238
indel_hom_alt 172370
indel_missing 19525
indel_total 946889
Expectation under HWE  393227.4873997697 421295.02520046063 112841.48739976964 927363.9999999999
Question 6:
{Does the difference in the number of homozygous alternate (or non-reference homozygous) and heterozygous SNVs and indels, make biological sense? Why, or why not}
The genotype counts seem to follow the Hardy Weinberg equilibrium expectations roughly by
eye. A formal chi-squared test is required to ensure that these
proportions are strictly in line with HWE.
-
Question 7:
python3 violate_MS.py  SNV_indel.biallelic.vcf 20
{How many variants clearly violate the rules of Mendelian segregation?}
6842 violations without looking at genotype quality. I did not looking
at sites with missing genotype calls.
-
Question 8:
{Describe four potential reasons that could explain the Mendelian violations.}
-de-novo mutations
-sequencing errors
-mapping artefacts
-somatic mosaicism or cell-line culturing artefacts
-
Question 9:
{How many variants now violate mendelian segregation after filtering? }
After filtering there are 1233 variants that violate Mendelian
segregation. This is about 1/6th of the original count, the filtering
appears to have helped remove some false-postives.
-
Comments:
{Things that went wrong or you can not figure out}
-
Suggestions:
{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}
-

