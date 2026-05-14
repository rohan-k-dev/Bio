# =========================================================
# IMPORT MODULES
# =========================================================

from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

from Bio import Phylo

import matplotlib.pyplot as plt


# =========================================================
# STEP 1 : CREATE ALIGNED SEQUENCES
# =========================================================

seq1 = SeqRecord(

    Seq("ATGCGTACGTA"),

    id="seq1"

)

seq2 = SeqRecord(

    Seq("ATGCGTACGTC"),

    id="seq2"

)

seq3 = SeqRecord(

    Seq("ATGCGTACGAG"),

    id="seq3"

)


print("Sequences Created Successfully.\n")


# =========================================================
# STEP 2 : CREATE MULTIPLE SEQUENCE ALIGNMENT
# =========================================================

alignment = MultipleSeqAlignment([

    seq1,
    seq2,
    seq3

])


print("Multiple Sequence Alignment Created.\n")


# =========================================================
# STEP 3 : CALCULATE DISTANCE MATRIX
# =========================================================

calculator = DistanceCalculator("identity")

distance_matrix = calculator.get_distance(alignment)

print("Distance Matrix Generated.\n")

print(distance_matrix)
print()


# =========================================================
# STEP 4 : CONSTRUCT PHYLOGENETIC TREE
# =========================================================

constructor = DistanceTreeConstructor()

tree = constructor.upgma(distance_matrix)

print("Phylogenetic Tree Constructed.\n")


# =========================================================
# STEP 5 : DISPLAY TREE
# =========================================================

print("Displaying Phylogenetic Tree...\n")

Phylo.draw(tree)


# =========================================================
# EXPECTED OUTPUT
# =========================================================

# Sequences Created Successfully.

# Multiple Sequence Alignment Created.

# Distance Matrix Generated.

# seq1    0.000000
# seq2    0.083333    0.000000
# seq3    0.166667    0.083333    0.000000

# Phylogenetic Tree Constructed.

# A phylogenetic tree window will open.
