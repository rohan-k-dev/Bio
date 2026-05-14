
from Bio import SeqIO

fasta_file = "example.fasta"

# Create and write data into FASTA file
with open(fasta_file, "w") as file:

    file.write(">seq1 This is the description for sequence 1\n")
    file.write("ATGCATGCGTACGTAGCTA\n\n")

    file.write(">seq2 This is the description for sequence 2\n")
    file.write("GCTAGCTAGCTAGCTA\n")


print("FASTA file created successfully.\n")


# =========================================================
# STEP 2 : READ FASTA FILE
# =========================================================

print("Reading FASTA File...\n")

# Parse FASTA file
for record in SeqIO.parse(fasta_file, "fasta"):

    # Print description/header
    print("Description:")
    print(record.description)

    # Print sequence
    print("Sequence:")
    print(record.seq)

    # Blank line
    print()

