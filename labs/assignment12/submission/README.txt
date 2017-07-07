Part 1
{Commands to run SNAP.pl on the YLR211C.alignment1.fasta and YLR211C.alignment2.fasta alignment files.}
perl SNAP.pl YLR211C.alignment1.fasta .
perl SNAP.pl YLR211C.alignment2.fasta .
-
Question 1:
{Which alignment is based on the nucleotide sequence and which is based on the protein sequence and why?}
alignment1 - protein sequence
alignment2 - nucleotide sequence
Sd and Nd are higher in alignment1 compared to alignment2 which
indicates that there's some alignment artefacts in alignment1, this
could be due to errors in the back translation from protein sequences due to the
redundancy of the genetic code.

{Which alignment suggests this gene has been evolving under positive selection?}
Alignment2 suggests the gene has been under positive selection since the
dNdS value is greater than one and hence more non-synonymous changes in
this gene compared to synonymous changes.
-
Part 2
{Command to run run_SNAP.py on all of the alignment files in the alignments subdirectory}
python3 run_SNAP.py  alignments/ part2/ 2>alignments.err 1>alignments.out
-
Question 2:
{What is the average dn/ds ratio?}
0.084
{How many genes have dn/ds > 1?}
three
YER179W 1.0982
YHR097C 1.1821
YML094W 3.4578
{What is the best evolutionary explanation for why YML094W has a dn/ds > 1?}
This gene is involved in tubulin assembly which is important for cell
division and motility both of which are potentially essential for fitness of an
organism.
-
Part 3
{Command to run plot_gene_length_vs_dnds.py on the output files from Part 2}
python3 plot_gene_length_vs_dnds.py  alignments.err alignments_all_dnds.txt
-
Question 3:
{What is the relationship between a gene’s dn/ds ratio and its length?}
As the length of the gene increases it's hard to find genes with higher
dn/ds values.
{What is the most likely explanation for this relationship?}
For long genes, if only certain parts of the genes are under positive
selection, say some specific domains, then this signal gets averaged
over by codons which are evolving neutrally.
{Propose a dn/ds-based method that would improve one’s ability to detect positive selection in long genes.}
As discussed in the lecture one could track dn/ds separately in each exon along the
gene, parts of the gene undergoing positive selection should show up by
this method.
-
Part 4
{Command to run calc_average_go_dnds.py on the S. cerevisiae GFF and output file from Part 2}
python3 calc_average_go_dnds.py  saccharomyces_cerevisiae.gff alignments_all_dnds.txt  > average_go_dnds.txt
-
Question 4:
{What GO term has the highest dn/ds ratio?}
GO:0034553      0.9213  YBR044C - mitochondrial respiratory chain complex II assembly
The next two terms are:
GO:0015631      0.6163333333333334 YEL003W,YGR078C,YLR200W,YML094W,YNL153C,YOR265W
GO:0016272      0.6153000000000001 YEL003W,YGR078C,YJL179W,YLR200W,YML094W,YNL153C
{Which genes are annotated with this GO?}
YBR044C
{What GO term has the lowest dn/ds?}
There's a tie for the bottom two
GO:0004347      0.0025  YBR196C - glucose-6-phosphate isomerase activity
GO:0051173      0.0025  YDR075W -  positive regulation of nitrogen compound metabolic process  
{What genes are annotated with this GO term?}
YBR196C
YDR075W
{Explain how you arrived at your answer.}
For each GO term, I looked at all the genes in the ontology for which I
had dnds values. I then computed the average dnds score for each of the
ontology terms.
-
Comments:
{Things that went wrong or you can not figure out}
-
 


