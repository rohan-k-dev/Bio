from Bio import AlignIO
import subprocess
import os

# Define sequences
seq1 = """>seq1
ATGCGTACGTA
"""

seq2 = """>seq2
ATGCGTACGTC
"""

seq3 = """>seq3
ATGCGTACGAG
"""

# Write sequences to FASTA file
with open("fasta8.fasta", "w") as f:
    f.write(seq1)
    f.write(seq2)
    f.write(seq3)

# Full path of muscle.exe
muscle_exe = os.path.join(os.getcwd(), "muscle.exe")

# Run MUSCLE alignment
subprocess.run([
    muscle_exe,
    "-align", "fasta8.fasta",
    "-output", "aligned_sequences.fasta"
], check=True)

# Read alignment
alignment = AlignIO.read("aligned_sequences.fasta", "fasta")

# Print result
print(alignment)

"""
===============================
DOWNLOAD MUSCLE.EXE INSTRUCTIONS
===============================

METHOD 1 (Direct Download)

1. Open:
   https://www.nologin.in/biopy

2. Download:
   muscle.exe

3. Move muscle.exe to your project folder.

Example:
C:\\Users\\rohan\\OneDrive\\Desktop\\biopython


-----------------------------------

METHOD 2 (Official MUSCLE Website)

1. Search on Google:
   muscle executable file install

2. Open:
   Installing MUSCLE - drive5drive5.com

3. On the right side click:
   MUSCLE v5 (state of the art MSA)

4. On the left side click:
   MUSCLE v5 (state of the art MSA)

5. Open:
   Latest Release

6. Download:
   muscle-win64.v5.3.exe

7. Rename file:
   muscle-win64.v5.3.exe
   to
   muscle.exe

8. Move muscle.exe to your project folder.

Example:
C:\\Users\\rohan\\OneDrive\\Desktop\\biopython


-----------------------------------

FINAL STEP

Keep these files in same folder:

1. final_8.py
2. muscle.exe

Then run:

py final_8.py
"""
