Part 1:
{Command line argument you used for filter_variants.py}
python3 filter_variants.py variant_to_barcode.txt  > filtered_variant_to_barcode.txt
-
Question 1:
{How many variants are not well represented by barcodes?}
six
-
Question 2:
{Why do you want to know barcode counts in plasmid DNA?}
This will help normalize the RNA counts, for example we might
be seeing more counts of a barcode in the RNA just because
there are more plasmids with this barcode.
-
Question 3:
{Command line argument you used for count_barcodes.py}
python3 count_barcodes.py  pDNA.fq filtered_variant_to_barcode.txt
python3 count_barcodes.py  cDNA.fq filtered_variant_to_barcode.txt
{How many reads in cDNA.fq are left after filtering?}
awk '{ sum += $2 } END { print sum }' cDNA_count.txt
52073
-
Part 2:
{Command line argument you used for analyze_MPRA.py}
python3 analyze_MPRA.py pDNA_count.txt cDNA_count.txt >  variant_fold_change.txt
join <(sort -k1,1 variant_fold_change.txt) <(sort -k1,1 variant_eQTL_results.txt)  | sort -k6,6  > join_op.txt
I used a p-value cutoff of 0.05
awk '$3 < 0.05' join_op.txt > join_op_filtered.txt
-
Question 4:
{eQTL of ENSG00000120071}
{# of variants}
16
{Causal variants?}
Three variants have a positive effect size direction
rs111511018
rs114812993
rs116967306
{eQTL of ENSG00000159202}
{# of variants}
6
{Causal variants?}
zero - None have the expected negative effect size.
{eQTL of ENSG00000184716}
{# of variants}
3
{Causal variants?}
2 variants have a positive effect size
rs3101443
rs3759791
-
Question 5:
{Possible reason?}
1. These eQTLs might be acting in a cell type specific way. K562 might not
be the best cell type to test the effects of these eQTLs.
2. Genomic context might be important and plasmids might not be reflecting
these.
{Way to improve in the study design?
1. Making genomic edits using perhaps CRISPR or integrating these oligos
into the genome to get at the genomic position effect.
2. Figuring out the right cell type to use and perhaps getting at those,
patient derived iPSCs might offer one alternative to get to those cells.
Comments:
{Things that went wrong or you can not figure out}
-
Suggestions:
{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}}
