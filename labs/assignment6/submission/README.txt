Question 1:
{Score for highest affinity binding site for the TF scoring matrix}
48.0
{Sequence(s) corresponding to highest affinity binding site for the TF scoring matrix}
G C T G C/T G C A C G
{Score for highest affinity binding site for the polymerase scoring matrix}
62.0
{Sequence(s) corresponding to highest affinity binding site for the polymerase scoring matrix}
G C A C G G C A C G
{Show your work for how you arrived at your answer and provide the command if you wrote a script.}
I took the row with the maximum score at each column and summed it up
manually.
-
Question 2:
{Command to run scan_sequence.py on the TF and promoter1}
python3 scan_sequence.py tf_score_matrix.txt  promoter1.txt 40
{Output of command}
orientation     position        sequence        score
forward 68      GCTATGCACG      45.00
reverse 963     GCTGTGCAGG      43.00
{Command to run scan_sequence.py on the TF and promoter2}
python3 scan_sequence.py tf_score_matrix.txt  promoter2.txt 40
{Output of command}
orientation     position        sequence        score
forward 181     GCTGCGCACG      48.00
No threshold-exceeding hits found in the reverse direction!
{Command to run scan_sequence.py on the polymerase and promoter1}
python3 scan_sequence.py polymerase_score_matrix.txt  promoter1.txt 45
{Output of command}
orientation     position        sequence        score
forward 102     CCACGGCACG      59.00
No threshold-exceeding hits found in the reverse direction!
{Command to run scan_sequence.py on the polymerase and promoter2}
python3 scan_sequence.py polymerase_score_matrix.txt  promoter2.txt 45
{Output of command}
orientation     position        sequence        score
forward 186     GCACGGCACG      62.00
No threshold-exceeding hits found in the reverse direction!
{Name of the promoter that you'd expect to be repressed by the TF}
promoter1
{Name of the promoter that you'd expect to be activated by the TF}
promoter2
{Explanation}
The transcription factor binds to both strands of promoter1, this could
result in an anti-sense transcript and a sense transcript which
hybridize and result in obstruction of the translational machinery.
-
Comments:
{Things that went wrong or you can not figure out}
-
Suggestions:
{What programming and/or genomics topics should the TAs cover in the next class that would have made this assignment go smoother?}

