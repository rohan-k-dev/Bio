# =========================================================
# IMPORT MODULES
# =========================================================

from Bio import Entrez
from Bio import SeqIO


# =========================================================
# STEP 1 : PROVIDE EMAIL
# =========================================================

# Replace with your email if needed

Entrez.email = "student@example.com"


# =========================================================
# STEP 2 : ACCESSION NUMBER
# =========================================================

# Example accession number

accession_number = "NM_001301717"

print("Fetching data from NCBI...\n")


# =========================================================
# STEP 3 : FETCH DATA FROM NCBI
# =========================================================

handle = Entrez.efetch(

    db="nucleotide",

    id=accession_number,

    rettype="gb",

    retmode="text"

)


# =========================================================
# STEP 4 : READ GenBank DATA
# =========================================================

seq_record = SeqIO.read(handle, "genbank")

handle.close()


# =========================================================
# STEP 5 : PRINT SEQUENCE DETAILS
# =========================================================

print("SEQUENCE INFORMATION\n")

print("Accession Number:")
print(seq_record.id)
print()

print("Description:")
print(seq_record.description)
print()

print("Organism:")
print(seq_record.annotations["organism"])
print()

print("Sequence:")
print(seq_record.seq)
print()

print("Length of Sequence:")
print(len(seq_record.seq))
print()

print("Features:")
print(seq_record.features)
print()


# =========================================================
# EXPECTED OUTPUT
# =========================================================

# Fetching data from NCBI...

# SEQUENCE INFORMATION

# Accession Number:
# NM_001301717

# Description:
# Homo sapiens ...

# Organism:
# Homo sapiens

# Sequence:
# ATGCGT....

# Length of Sequence:
# 1000+

# Features:
# [SeqFeature(...)]



#-------------------------------------------------------------------------


#import os
#import certifi

#os.environ['SSL_CERT_FILE'] = certifi.where()


