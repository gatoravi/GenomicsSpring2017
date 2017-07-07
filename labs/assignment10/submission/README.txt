Question 1:
{Assumptions of Wright-Fisher}
- Generations are non-overlapping
- Random mating
- No selection
- Only two alleles at a locus
- Mutation does not occur

-
Part 1
{Usage statement for dominant model}
python3 wrightfisher.py 100 1000 3 dominant
-
Question 2:
{Fitness value}
3
{Explanation}
The fitness of the hets and homs is three times
that of the non-mutant genotype. The mutant allele
rises up in frequency quite fast and I get probabilities
around 90% with a fitness of 3 in the dominant case.
-
Part 2
{Usage statement for recessive model}
python3 wrightfisher.py 100 1000 3 recessive
-
Question 3:
{Fitness value}
N/A
{Explanation}
In the recessive case the probability of the first het getting
picked up is so low that it just dies out no matter what the fitness
of that allele when recessive is.
I'm not able to get fixation 90% of the time with any fitness. The
probability of picking the mutant allele in the first generation 
is 1/200 under this fitness.
-
Comments:
{Things that went wrong or you can not figure out}
