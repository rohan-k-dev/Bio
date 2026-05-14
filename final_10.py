
# =========================================================
# IMPORT MODULES
# =========================================================

from Bio import PDB


# =========================================================
# STEP 1 : CREATE PDB DOWNLOADER
# =========================================================

pdbl = PDB.PDBList()


# =========================================================
# STEP 2 : DOWNLOAD PDB FILE
# =========================================================

pdb_id = "1TUP"

print("Downloading PDB Structure...\n")

pdbl.retrieve_pdb_file(

    pdb_id,

    pdir=".",

    file_format="pdb"

)


print("PDB File Downloaded Successfully.\n")


# =========================================================
# STEP 3 : PARSE PDB FILE
# =========================================================

parser = PDB.PDBParser(QUIET=True)

pdb_file = f"pdb{pdb_id.lower()}.ent"

structure = parser.get_structure(

    "protein",

    pdb_file

)


print("Protein Structure Parsed Successfully.\n")


# =========================================================
# STEP 4 : SELECT MODEL
# =========================================================

model = structure[0]

print("Model Selected.\n")


# =========================================================
# STEP 5 : SELECT CHAIN
# =========================================================

chain = model["A"]

print("Selected Chain:")
print(chain.id)
print()


# =========================================================
# STEP 6 : DISPLAY RESIDUES
# =========================================================

print("Residues in Chain A:\n")

for residue in chain:

    print(residue)


# =========================================================
# STEP 7 : SAVE STRUCTURE
# =========================================================

io = PDB.PDBIO()

io.set_structure(structure)

io.save("output.pdb")


print("\nProtein Structure Saved as output.pdb")


# =========================================================
# GENERATED FILES
# =========================================================

# 1. pdb1tup.ent
# 2. output.pdb


# =========================================================
# VISUALIZATION
# =========================================================

# To visualize 3D structure:
# Open output.pdb using:

# 1. PyMOL
# 2. UCSF Chimera
# 3. ChimeraX


# =========================================================
# EXPECTED OUTPUT
# =========================================================

# Downloading PDB Structure...

# PDB File Downloaded Successfully.

# Protein Structure Parsed Successfully.

# Model Selected.

# Selected Chain:
# A

# Residues in Chain A:

# <Residue MET het=  resseq=1 icode= >
# <Residue GLY het=  resseq=2 icode= >
# ...

