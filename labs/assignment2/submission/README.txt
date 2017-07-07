Part 1:
Question 1:
The 'nr' database consists of non-redundant proteins. This is a pretty
comprehensive list of proteins from multiple sources. If two proteins
have the exact same amino acid sequences, these are stored only once
in this database. For our purposes this is fine since we are only
interested in knowing what our coding sequence represents and not
necessarily which source the annotation came from.

-
Question 2:
163 hits have an e-value less than 1. There are 212 hits
in total.
-
Question 3:
gene genus species - rap1p  in Saccharomyces arboricola H-6
score - 1294
%identity - 85%
-
Question 4:
164 hits with an e-value less than 1. I got one more hit with BLOSUM80
instead of BLOSUM62. In total there are 204 hits.

The number of total hits is fewer since we are using scores obtained
from proteins with greater identity(80% compared to 62%), so this is
in a sense more stringent. However, since most of the hits are from
the same species anyway this number doesn't change dramatically.
-
Question 5:
gene genus species - rap1p  in Saccharomyces arboricola H-6
score - 1352
%identity - 85%
The score increases, BLOSUM80 alignments perhaps reflect the relationship
between these two proteins better than BLOSUM62.
-
Question 6:
It remains the same.
DNA-binding transcription factor RAP1 [Saccharomyces cerevisiae S288c]
Score - 1536 with BLOSUM80, 1462 with BLOSUM62
%identity - 100%
BLOSUM80 results in a higher score since this is the same protein and
a higher identity alignment reflects the truth.
-

Question 7:
Now there are 180 hits in total and 151 with a score less than 1.
The number of hits decreases with a decrease in gap existence penalty.
This could be because since gaps are now less costly more gaps are
opened and this results in poorer matches.

-
Question 8:
The score of the closest ortholog decreased to 1163 from 1294, this
could be because of more gaps now in the alignment which reduce the
quality of the alignment.

-
Question 9:
If I lowered the word length I would expect the search to take more time
since there are likely to be more matches by chance and there are more
scores to be computed.
-
Question 10:
Yes, online BLAST does take quite a while to compute.
-
Question 11:
bowtie2-build chr22.fa chr22_index
bowtie2 -x chr22_index -U assignment2/reads.fq -p 2 -S assignment2_reads.sam 2>report.tsv

How many reads map uniquely to chr22? 7115
How many reads map to multiple locations? 10126
How many reads were unmappable? 9421
-
Question 12:
Enrichment of C,G
Dinucleotides, enrichment of CG

Nucleotide Enrichment
A: 0.9868179303244734
C: 1.1621086823926658
G: 1.1913045461338783
T: 0.7381010245259338

Dinucleotide Enrichment
AA:1.0197035873088285
AC:0.9647768456801074
AG:0.7866719285732388
AT:1.151799970311261
CA:0.9716689778022366
CC:1.1726605334076758
CG:6.3040271688166865
CT:0.7485472431109453
GA:1.3738922540149192
GC:1.2330486352231542
GG:1.3544449231653024
GT:0.7434726411029727
TA:0.5470850123763421
TC:1.2076353160824866
TG:0.8043122893276226
TT:0.4258362830986193

Description of how enrichment scores were calculated
I used the observed frequency in human chr20 from homework1
as my baseline expectation. I then divided the observed frequency
in this dataset by my expectation to arrive at the enrichment.
I assumed that this data-set is from a human sample or from
a sample with a genome of similar base composition.

Assay, Explanation
The high GC content suggests that this dataset could be from the
coding regions of the genome, hence the assay could either be exome
sequencing or RNA sequencing.

-
Looking at the local BLAST results, the sequences appear to be from the dog genome since the top matches
are all to the 'Canis familiaris' species.

Extra Credit 1:
We use BLASTn since we'd like to search the nucleotide database
with a nucleotide query. We don't know if this query lies in a coding
frame. If we did we could search a protein database with the translated
nucleotides using BLASTx.

Command used:
blastn -query assignment2/unknown.fsa -db nt -remote  > blast_output.txt
-
