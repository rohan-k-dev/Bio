# =========================================================
# IMPORT MODULES
# =========================================================

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation


# =========================================================
# STEP 1 : CREATE DNA SEQUENCE
# =========================================================

dna_sequence = Seq("ATGCGTACGTAGCTAGCTAG")

print("DNA Sequence Created:")
print(dna_sequence)
print()


# =========================================================
# STEP 2 : CREATE SeqRecord OBJECT
# =========================================================

record = SeqRecord(

    dna_sequence,

    id="seq1",

    name="Example_Gene",

    description="An example DNA sequence for gene annotation."

)

print("SeqRecord Object Created Successfully.\n")


# =========================================================
# STEP 3 : ADD ANNOTATIONS
# =========================================================

record.annotations["gene"] = "ExampleGene"

record.annotations["function"] = "Hypothetical protein"

record.annotations["organism"] = "Synthetic organism"

print("Annotations Added Successfully.\n")


# =========================================================
# STEP 4 : ADD FEATURE (GENE LOCATION)
# =========================================================

gene_feature = SeqFeature(

    FeatureLocation(0, 21),

    type="gene",

    qualifiers={
        "gene": "ExampleGene"
    }

)

record.features.append(gene_feature)

print("Gene Feature Added Successfully.\n")


# =========================================================
# STEP 5 : MODIFY ANNOTATION
# =========================================================

record.annotations["function"] = "Hypothetical protein with modified function"

print("Function Annotation Modified.\n")


# =========================================================
# STEP 6 : PRINT UPDATED SeqRecord
# =========================================================

print("UPDATED SeqRecord INFORMATION\n")

print("ID:")
print(record.id)
print()

print("Name:")
print(record.name)
print()

print("Description:")
print(record.description)
print()

print("Annotations:")
print(record.annotations)
print()

print("Features:")
print(record.features)
print()


# =========================================================
# EXPECTED OUTPUT
# =========================================================

# DNA Sequence Created:
# ATGCGTACGTAGCTAGCTAG

# SeqRecord Object Created Successfully.

# Annotations Added Successfully.

# Gene Feature Added Successfully.

# Function Annotation Modified.

# UPDATED SeqRecord INFORMATION

# ID:
# seq1

# Name:
# Example_Gene

# Description:
# An example DNA sequence for gene annotation.

# Annotations:
# {'gene': 'ExampleGene',
#  'function': 'Hypothetical protein with modified function',
#  'organism': 'Synthetic organism'}

# Features:
# [SeqFeature(SimpleLocation(ExactPosition(0),
# ExactPosition(21)), type='gene')]
