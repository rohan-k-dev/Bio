# =========================================================
# PROGRAM 3
# Write DNA Sequence and Annotations to GenBank File
# =========================================================

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO


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

    description="Example gene sequence",

    annotations={
        "molecule_type": "DNA"
    }

)


# =========================================================
# STEP 3 : ADD FEATURE / ANNOTATION
# =========================================================

gene_feature = SeqFeature(

    FeatureLocation(0, len(dna_sequence)),

    type="gene",

    qualifiers={
        "gene": ["ExampleGene"],
        "function": ["Hypothetical protein"]
    }

)

record.features.append(gene_feature)

print("Gene Feature Added.\n")


# =========================================================
# STEP 4 : WRITE TO GENBANK FILE
# =========================================================

output_file = "example_output.gb"

with open(output_file, "w") as file:

    SeqIO.write(record, file, "genbank")


print("GenBank file written successfully.\n")


# =========================================================
# STEP 5 : READ GENBANK FILE
# =========================================================

print("Reading GenBank File...\n")

with open(output_file, "r") as file:

    content = file.read()

    print(content)


# =========================================================
# END OF PROGRAM
# =========================================================