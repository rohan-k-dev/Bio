# =========================================================
# IMPORT MODULE
# =========================================================

from Bio.Align import PairwiseAligner


# =========================================================
# STEP 1 : DEFINE DNA SEQUENCES
# =========================================================

seq1 = "AGTACACTGGT"

seq2 = "AGTACGCTGGT"

print("Sequence 1:")
print(seq1)
print()

print("Sequence 2:")
print(seq2)
print()


# =========================================================
# STEP 2 : CREATE ALIGNER OBJECT
# =========================================================

aligner = PairwiseAligner()

print("PairwiseAligner Object Created.\n")


# =========================================================
# STEP 3 : PERFORM ALIGNMENT
# =========================================================

alignments = aligner.align(seq1, seq2)

print("Alignment Performed Successfully.\n")


# =========================================================
# STEP 4 : DISPLAY ALIGNMENT
# =========================================================

print("ALIGNED SEQUENCES\n")

print(alignments[0])


# =========================================================
# STEP 5 : DISPLAY ALIGNMENT SCORE
# =========================================================

print("Alignment Score:")

print(alignments[0].score)


# =========================================================
# EXPECTED OUTPUT
# =========================================================

# Sequence 1:
# AGTACACTGGT

# Sequence 2:
# AGTACGCTGGT

# PairwiseAligner Object Created.

# Alignment Performed Successfully.

# ALIGNED SEQUENCES

# target            0 AGTACA-CTGGT 11
#                   0 |||||--||||| 12
# query             0 AGTAC-GCTGGT 11

# Alignment Score:
# 10.0
