from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Phylo

# Load Clustal alignment
alignment = AlignIO.read("aligned_sequences.aln", "clustal")

# Calculate distance matrix
calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

print(distance_matrix)

# Construct tree
constructor = DistanceTreeConstructor()
tree = constructor.upgma(distance_matrix)

# Draw tree
Phylo.draw(tree)