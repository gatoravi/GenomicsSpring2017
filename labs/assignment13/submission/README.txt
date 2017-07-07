Usage:
{How to run neutral_rate.py}
clustalw -INFILE=PRE1.fa -ALIGN
python3 neutral_rate.py PRE1.aln
-
Question 1:
{Fraction of wobble positions conserved}
0.46
This is a conservative estimate since I only looked at
the third base of each codon without specifically looking
at which amino acid the codon codes for. Anything that is
found significant at this threshold must pass a more carefully
calculated threshold.
-
Question 2
{Cutoff for 10bp sequence conserved}
>= 8 positions
{Explanation}
I used a binomial test in R. The null hypothesis is that
the prob of conserved sites is 0.46, the alternative hypothesis
is that the proportion of conserved sites > 0.46. For eight or
more conserved positions the p-value is less than the cutoff of 0.05
> binom.test(8, 10, 0.46, alternative="greater")

           Exact binomial test

data:  8 and 10
number of successes = 8, number of trials = 10, p-value = 0.03171
alternative hypothesis: true probability of success is greater than 0.46
95 percent confidence interval:
 0.4930987 1.0000000
sample estimates:
probability of success
                   0.8
-
Question 3:
{Number of regions}
Two
{S_cer_consreved.txt output}
Start Stop Sequence
555 570 TTCACGGTGGCAAAA
570 585 AATAAAGAAAAAGTG
-
Question 4:
{Answer here}
While using the entire promoter sequence 90 putative sites were
predicted as possible binding sites.

With just the conserved sequence one of them(the first, posn 555 - 570)
found a binding site for RPN4 as shown below:

Model ID    Model name    Score    Relative score    Start    End
Strand    predicted site sequence
MA0373.1    RPN4     9.835     0.93083645335212     6     12     1
GGTGGCA

According to the Saccharomyces genome database, RPN4 is a transcription
factor that binds to proteaosome genes, these makes sense if PRE1 is
involved in yeast proteasome assembly.
-
Comments:
{Things that went wrong or you can not figure out}
-
