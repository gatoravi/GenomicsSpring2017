Part 1.0
{Command for running analyze_WGBS_methylation.py}
python3 analyze_WGBS_methylation.py BGM_WGBS.bed
{Copy your output files BGM_WGBS_CpG_methylation.bed, BGM_WGBS_methylation_distribution.png, and BGM_WGBS_CpG_coverage_distribution.png to your submissions directory}
-
Question 1:
{What does DNA methylation look like across chromosome 21?}
Majority  of the sites with greater than zero reads appear to
be methylated. Most of the sites are close to 1.0 A small 
fraction of the sites appear to be unmethylated.
-
Question 2:
{What does the CpG coverage look like across chromosome 21?}
The CpG coverage has an average of around 27X. With increasing
coverage, the number of sites at that coverage keeps dropping.
-
Question 2.1:
{What fraction of the CpGs have 0X coverage?}
8.4% of CpGs have zero coverage
-
Part 1.1
{Command for creating a bed file with the average CpG methylation level in each CGI.}
bedtools intersect -a  BGM_WGBS_CpG_methylation.bed -b CGI.bed  -wb > intersect1.bed
bedtools groupby -i intersect1.bed -g 5,6,7,8 -c 4 -o mean > WGBS_CGI_methylation.bed
{Copy WGBS_CGI_methylation.bed to your submissions directory}
-
Part 1.2
{Command for plotting the distribution of average CGI methylation levels}
python analyze_CGI_methylation.py average_cgi_methylation.txt WGBS_CGI_methylation_distribution.png 1
{Copy analyze_CGI_methylation.py and WGBS_CGI_methylation_distribution.png to your submissions directory}
-
Question 3:
{What does DNA methylation look like for CpGs in CGIs? How does it compare to all the CpGs on chromosome 21?}
A lot of the CGIs appear to have methylation values close to zero. The
CpGs across chromosome21 had fewer sites with very low methylation values.
-
Part 1.3.0
Gene promoters
{Command for generating the promoter bed file}
python generate_promoters.py refGene.bed > refGene_promoters.bed
{Justification for promoter definition}
Promoters are defined as 1000 basepairs upstream of the transcription
start site. For genes transcribed on the +ve strand this is
gene_start-1000, for genes transcribed on the -ve strand this is
gene_end+1000

{Copy generate_promoters.py and refGene_promoters.bed to your submissions directory}
-
Promoter-CGI and non-promoter-CGI
{Commands for generating promoter-CGI and non-promoter-CGI bed files}
bedtools intersect -a CGI.bed -b refGene_promoters.bed  > promoter_CGI.bed
bedtools intersect -a CGI.bed -b refGene_promoters.bed -v  > non_promoter_CGI.bed
{Justification for overlapping criteria}
Any CpGs that completely overlapped with a promoter region was
considered a promoter CGI and any region that had no overlap with
a promoter was considered a non promoter CGI. This definition is a
bit simplistic but with the large number of CGIs, the methylation patterns should
be visible.
{Commands for calculating the average CpG methylation for each promoter-CGI and non-promoter-CGI}
bedtools intersect -a BGM_WGBS_CpG_methylation.bed -b promoter_CGI.bed -wb > intersect3.bed
bedtools groupby -i intersect3.bed -g 5,6,7,8 -c 4 -o mean > average_promoter_CGI_methylation.bed

bedtools intersect -a BGM_WGBS_CpG_methylation.bed -b non_promoter_CGI.bed -wb > intersect4.bed
bedtools groupby -i intersect4.bed -g 5,6,7,8 -c 4 -o mean > average_non_promoter_CGI_methylation.bed
{Commands for running analyze_CGI_methylation.py on average_promoter_CGI_methylation.bed and average_non_promoter_CGI_methylation.bed}
python analyze_CGI_methylation.py average_promoter_CGI_methylation.bed average_promoter_CGI_methylation.png 4
python analyze_CGI_methylation.py average_non_promoter_CGI_methylation.bed average_non_promoter_CGI_methylation.png 4
{Copy refGene_promoters.bed, promoter_CGI.bed, non_promoter_CGI.bed average_promoter_CGI_methylation.bed, average_non_promoter_CGI_methylation.bed, average_promoter_CGI_methylation.png and average_non_promoter_CGI_methylation.png to your submissions directory}
-
Question 4:
{How do the DNA methylation profiles of promoter-CGIs and non-promoter-CGIs differ?}
Promoter CGIs are less methylated compared to non-promoter CGIs, huge
peak near zero.
-
Part 1.3.1
{Commands for calculating CpG frequency for each promoter type}
bedtools getfasta -fi hg19_chr21.fa -bed promoter_CGI.bed -fo promoter_CGI.fa
bedtools getfasta -fi hg19_chr21.fa -bed non_promoter_CGI.bed -fo non_promoter_CGI.fa
{CpG frequencies for each promoter type}
python3 nuc_count_multisequence_fasta.py  promoter_CGI.fa
CG:0.10751309514502384
python3 nuc_count_multisequence_fasta.py non_promoter_CGI.fa
CG:0.09070296563627805

-
Question 5:
{What is a possible biological explanation for the difference in CpG frequencies?  Interpret your results from parts 1.3.0 and 1.3.1: what are the “simple rules” for describing regulation by DNA methylation in promoters?}
The methylated C's are easier to de-aminate into T's. Since promoters
are less methylated the frequency of CpGs are higher since these are
less likely to deaminate.
Methylation of promoters is a mechanism to turn the genes off since
these block the binding of DNA polymerase.
-
Part 2
{Commands to calculate CGI RPKM methylation scores}
perl bed_reads_RPKM.pl CGI.bed BGM_MRE.bed > MRE_CGI_RPKM.bed
perl bed_reads_RPKM.pl CGI.bed BGM_MeDIP.bed > MeDIP_CGI_RPKM.bed
{Command to generate the correlation plots}
python3 compare_methylome_technologies.py MeDIP_CGI_RPKM.bed MRE_CGI_RPKM.bed WGBS_CGI_methylation.bed
{Correlations for each comparison}
MEDIP vs WGBS - 0.736226209607
MRE vs MEDIP - 0.0310817243079
MRE vs WGBS -  -0.445764041562
{Justification for chosen correlation metric}
I used Pearsons correlation coefficient since I expect a linear
relationship between the methylation metrics from different
technologies.
{Copy compare_methylome_technologies.py, MeDIP_CGI_RPKM.bed, MRE_CGI_RPKM.bed MeDIP_CGI_RPKM_vs_MRE_CGI_RPKM.png, MeDIP_CGI_RPKM_vs_WGBS_CGI_methylation.png, and MRE_CGI_RPKM_vs_WGBS_CGI_methylation.png to your submissions directory}
-
Question 6:
{How do MeDIP-seq and methylation correlate? How do MRE-seq and methylation correlate? How do MeDIP-seq and MRE-seq correlate?}
MEDIP and WGBS are strongly positively correlated.
MRE vs MEDIP don't correlate, correlation is close to zero.
MRE and WGBS are negatively correlated.
The negative correlation between MRE-seq and the remaining two
technologies is because MREseq interrogates unmethylated CpG's
whereas the other two techniques look at methylated CpG's.
The lower correlation is probably due to the outliers.
-
Outliers
{Answers to outlier questions}
Outlier that was removed - chr21   9825442 9826296
There is a (CGG)n repeat at this locus, the presence of the repeat
might result in enriched readcounts at this location.
{If applicable: correlations for each comparison}
MeDIP_CGI_RPKM_outliers_removed_vs_MRE_CGI_RPKM_outliers_removed
-0.604616805487
MeDIP_CGI_RPKM_outliers_removed_vs_WGBS_CGI_methylation_outliers_removed
0.80862567978
MRE_CGI_RPKM_outliers_removed_vs_WGBS_CGI_methylation_outliers_removed
-0.788756163048
{If applicable: copy the updated figures to your submissions directory}
-
Comments:
{Things that went wrong or you can not figure out}
-
Suggestions:
{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}
-
Extra credit
{Commands for running bed_reads_RKPM.pl}
perl bed_reads_RPKM.pl promoter_CGI.bed BGM_H3K4me3.bed > H3K4me3_RPKM_promoter_CGI.bed
perl bed_reads_RPKM.pl non_promoter_CGI.bed BGM_H3K4me3.bed > H3K4me3_RPKM_non_promoter_CGI.bed
{Command for running analyze_H3K4me3_scores.py}
{Copy analyze_H3K4me3_scores.py, H3K4me3_RPKM_promoter_CGI.bed, H3K4me3_RPKM_non_promoter_CGI.bed, and H3K4me3_RPKM_promoter_CGI_and_H3K4me3_RPKM_non_promoter_CGI.png}
-
Question EC.1:
{How does the H3K4me3 signal differ in promoter-CGIs and non-promoter-CGIs?}
H3K4me3 is higher in the promoters compared to the non-promoters.
H3K4me3 is a promoter mark, it functions by recruiting chromatin
remodeling proteins which open chromatin and enable transcription.
-
Question EC.2:
{What are some better alternatives to model MeDIP-seq data and MRE-seq data instead of using RPKM? Explain.}
One could use a different normalized version of counts such as TMM or
TPM. These will statistically  model for differences in counts between different
regions and enable comparisons between libraries.
-
Question EC.3:
{What would be a better way to compare H3K4me3 values instead of using boxplots? Explain.}
One could use histograms or perform a t-test to compare the average
 of the two groups.
-
