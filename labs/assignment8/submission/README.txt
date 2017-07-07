Question 1:
python3 call_orfs.py contigs.fna
{Number of ORFs from call_orfs.py}
68
-
Question 2:
{Explanation of each MetaGeneMark flag}
Commands used:
gmhmmp -a -d -f G -m /home/assignments/assignment8/2017_metagenemark/MetaGeneMark_v1.mod -o mgm_predictions.gff /home/assignments/assignment8/contigs.fna
perl aa_from_gff.pl mgm_predictions.gff  > mgm_orfs.faa
perl nt_from_gff.pl mgm_predictions.gff  > mgm_orfs.fna

We use -a to get the amino-acid sequences, -d to get the nucleotide
sequences of the ORFs. -G is used to get the output in the GFF format.
The model file is specified with -m. The output file is specified with
-o. The last argument is the fasta file with the contigs.

I might have used -A and -D to directly split the amino acids and nucleotides and
avoided the GFF output with -o and -G.
-
Question 3:
{Number of ORFs from MetaGeneMark}
There are 19 ORFs from MetaGeneMark
-
Question 4:
python3 compare_orf_callers.py mgm_orfs.faa all_proteins.faa
{Number of ORFs shared between MetaGeneMark and call_orfs.py output}
9
{Number of ORFs unique to call_orfs.py output}
59
{Number of ORFs unique to MetaGeneMark output}
10
{Interpretation of your results}
Some of the MGM results seem to consider smaller than 100 b.p results.
Some of the ORFs that MGM finds are not necessarily the longest ORF
when there are multiple start codons.
GeneMark uses probabilistic models that take into account codon
frequencies and nucleotide frequencies. These might make the
predictions more accurate and perhaps explain the fewer number of ORFs
from GeneMark.
-
Question 5:
 blastp -db /db/CARD.faa -query mgm_orfs.faa -out blast_to_card.txt -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore slen stitle"
{qseqid}
The sequence ID of the query sequence
{sseqid}
The sequence ID of the subject in the db.
{pident}
Percent identical matches
{length}
Alignment length
{mismatch}
Number of mismatches
{gapopen}
Number of gap openings
{qstart}
Start of the alignment in the query
{qend}
End of the alignment in the query
{sstart}
Start of the alignment in the subject
{send}
End of the alignment in the subject
{evalue}
Expected hits of similar quality found by chance
{bitscore}
Score reflecting sequence quality
{slen}
Subject sequence length
{stitle}
Subject title
-
Question 6:
python3 count_ar_genes_from_blast.py  blast_to_card.txt  > blast_to_card_filtered.txt
{Number of genes in BLAST output}
526
{Number of genes after filtering in the Python script}
11
-
Question 7:
{Use1 and how you would go about executing it}
Creation of multiple alignments of amino acid sequences:
hmmalign globins4.hmm tutorial/globins45.fa

{Use2 and how you would go about executing it}
Find distantly related DNA sequences within a sequence family, i.e with a
bit of sequence divergence.
Use nhmmer or nhmmscan,
hmmbuild MADE1.hmm tutorial/MADE1.sto
nhmmer MADE1.hmm tutorial/dna target.fa > MADE1.out
hmmscan minifam tutorial/7LESS DROME
-
Question 8:
 hmmscan --cut_ga --tblout resfams_annotations.txt  /home/assignments/assignment8/Resfams/resfams.hmm mgm_orfs.faa > resfams_log.txt
{Total number of genes annotated by Resfams}
Four
{Comparison of the number of genes annotated by Resfams and the number of genes annotated by BLAST}
Blast identified eleven genes. This indicates that the hmmscan model
might be looking for more stringent matches whereas perhaps the BLAST
results are bit more permissive. It's hard to compare these identifiers
directly because of apparent different nomenclature.
-
Comments:
{Things that went wrong or you can not figure out}
-
Suggestions:
{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}


