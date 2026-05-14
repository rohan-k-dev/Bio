# =========================================================
# IMPORT MODULES
# =========================================================

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation


# =========================================================
# STEP 1 : CREATE FASTA FILE
# =========================================================

fasta_file = "fasta_1.fasta"

with open(fasta_file, "w") as file:

    file.write(">seq1 Example sequence description\n")
    file.write("ATGCGTACGTAGCTAGCTAG\n")


print("FASTA file created successfully.\n")


# =========================================================
# STEP 2 : FUNCTION TO CONVERT FASTA → GENBANK
# =========================================================

def convert_fasta_to_genbank(fasta_file, genbank_file):

    # List to store records
    records = []

    # Read FASTA file
    for record in SeqIO.parse(fasta_file, "fasta"):

        # Extract sequence and description
        sequence = record.seq
        description = record.description

        # Create SeqRecord object
        genbank_record = SeqRecord(

            sequence,

            id=record.id,

            name="Example_Gene",

            description=description,

            annotations={
                "molecule_type": "DNA"
            }

        )

        # Add gene feature
        gene_feature = SeqFeature(

            FeatureLocation(0, len(sequence)),

            type="gene",

            qualifiers={
                "gene": ["ExampleGene"],
                "function": ["Hypothetical protein"]
            }

        )

        # Append feature
        genbank_record.features.append(gene_feature)

        # Add record to list
        records.append(genbank_record)

    # Write GenBank file
    with open(genbank_file, "w") as output_handle:

        SeqIO.write(records, output_handle, "genbank")

    print("GenBank file created successfully.\n")


# =========================================================
# STEP 3 : DEFINE OUTPUT FILE
# =========================================================

genbank_file = "example_output.gb"


# =========================================================
# STEP 4 : CALL FUNCTION
# =========================================================

convert_fasta_to_genbank(fasta_file, genbank_file)


# =========================================================
# STEP 5 : DISPLAY GENBANK FILE CONTENTS
# =========================================================

print("Reading GenBank File...\n")

with open(genbank_file, "r") as file:

    content = file.read()

    print(content)


# =========================================================
# GENERATED FILES
# =========================================================

# 1. fasta_1.fasta
# 2. example_output.gb


# =========================================================
# EXPECTED OUTPUT
# =========================================================

# FASTA file created successfully.

# GenBank file created successfully.

# Reading GenBank File...

# LOCUS       seq1
# DEFINITION  seq1 Example sequence description
# ACCESSION   seq1

# FEATURES             Location/Qualifiers
#      gene            1..21
#                      /gene="ExampleGene"
#                      /function="Hypothetical protein"

