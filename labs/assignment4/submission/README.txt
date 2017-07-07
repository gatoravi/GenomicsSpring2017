Assignment 4 Due February 15 at 10am

Please provide the exact command line arguments you used to generate your results.
{How to run gene_expression.py}
python3 gene_expression.py raw_counts.txt
-
Question 1:
{How many genes are left after removing genes with zero expression in all samples?}
43758
-
Question 2:
{How many genes are left after removing genes where 6 or more samples have cpm < 1?}
16250
-
Question 3:
{What is the range of library sizes (min, max)?}
min - 8,743,525, max - 12,461,148
-
Question 4:
{What is the range of library sizes (min, max) after normalization?}
min - 10803129.713, max - 12018243.0433
-
Question 5:
{Compare the two library size bar charts you made. How did the distribution of library sizes change after normalization?}
After normalization the library sizes look more even across samples
-
{Briefly discuss why it is important to normalize your RNA-seq data.}
Normalization enables comparison across samples/conditions. Without
normalization, differences in library size, variability in gene
expression within a condition can pull up false positives as
differentially expressed genes.

-
Question 6:
{What are the top ten differentially expressed genes according to your FLD analysis? (Copy and paste your function?s output.)}
Top 10 FLD genes:  ['ENSG00000181163', 'ENSG00000135486',
'ENSG00000230593', 'ENSG00000124496', 'ENSG00000164402',
'ENSG00000237238', 'ENSG00000239474', 'ENSG00000279110',
'ENSG00000100519', 'ENSG00000165424']
-
{Do these genes make sense given the tissue and groups in the experiment?}
NPM1 is associated with ribonucleoprotein structure.
HNRNPA1 is a ribonucleoprotein
TRERF1 is a zinc-finger transcriptional regulating protein
KLHL41 is involved in skeletal muscle development
Most of these proteins are related to transcriptional or translational
regulation. These don't seem to be specifically related to insulin or
glucose metabolism, however perhaps the basic cellular activities
perform differently in the post-exercise group.
-
Question 7:
{Does your result point toward one gene with large effect or many genes with small effects?}
Many genes with small effects.
-
{Does RNA-seq expression data always give researchers a clear answer?}
No the results are usually subtle, multiple replicates are needed to
confirm the findings since gene expression is dynamic.
-
Question 8:
{How does the study design of this experiment relate to the assumptions made when studying gene expression data?}
Since we assume that there is a standard expression level and changes in
expression profile correspond to important differences multiple
replicates are usually needed to confirm the findings.
This study design has 6 individuals before the exercise regimen and 6
after the exercise regimen. There are multiple samples in each group.
-
Question 9:
{If you were going to spend time and money following up on one of these top ten genes, what would be your candidate and why? (There could be many correct answers.)}
I would follow up on KLHL41 since it is involved in skeletal muscle
development.
-
Extra credit 1:
{What do you expect to see?}
I expected to see two groups, before samples and after samples
-
Extra credit 2:
{What did you actually see? If you did not find what you expected, what sorts of variation could account for this?}
One of the after samples clustered with the before samples, this was
unexpected. Several confounders could result in this, one that comes
to mind is if the effect of regimen varies say by age and if one of the
subjects is an outlier by age and if the effect of exercise is small
on this subject we wouldn't expect his before/after samples to cluster
separately.
-
Comments:
{Things that went wrong or you cannot figure out}
-
Suggestions:
{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}
-


