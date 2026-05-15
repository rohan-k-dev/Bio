from Bio import PDB

# Step 1: Create a PDB parser
parser = PDB.PDBParser(QUIET=True)

# Step 2: Load a protein structure from a PDB file
pdb_id = "1TUP"   # Example PDB ID

structure = parser.get_structure(
    "protein",
    f"pdb/{pdb_id}.pdb"
)

# Step 3: Access model and chain
model = structure[0]      # First model
chain = model['A']        # Chain A

# Step 4: Print residues in chain
print(f"Chain {chain.id}:")

for residue in chain:
    print(residue)

# Step 5: Save structure to a new PDB file
io = PDB.PDBIO()
io.set_structure(structure)
io.save("output.pdb")

print("\nStructure saved as output.pdb")