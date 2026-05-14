# =====================================================
# PROGRAM 1
# Seq Class Operations using BioPython
# =====================================================

# Import Seq class
from Bio.Seq import Seq


# =====================================================
# STEP 1 : Create DNA Sequence
# =====================================================

dna_sequence = Seq("ATGCTAGCTAGCTAGCTG")

print("Original DNA Sequence:")
print(dna_sequence)


# =====================================================
# STEP 2 : Slice Sequence from index 3 to 10
# =====================================================

sliced_sequence = dna_sequence[3:11]

print("\nSliced Sequence:")
print(sliced_sequence)


# =====================================================
# STEP 3 : Concatenate with another sequence
# =====================================================

another_sequence = Seq("GGCTAG")

concatenated_sequence = sliced_sequence + another_sequence

print("\nConcatenated Sequence:")
print(concatenated_sequence)


# =====================================================
# STEP 4 : Transcribe DNA to RNA
# =====================================================

rna_sequence = concatenated_sequence.transcribe()

print("\nRNA Sequence:")
print(rna_sequence)


# =====================================================
# STEP 5 : Translate RNA to Protein
# =====================================================

# Trim RNA sequence so its length becomes multiple of 3
trimmed_rna = rna_sequence[:len(rna_sequence) - (len(rna_sequence) % 3)]

protein_sequence = trimmed_rna.translate()

print("\nProtein Sequence:")
print(protein_sequence)


# =====================================================
# END OF PROGRAM
# =====================================================
