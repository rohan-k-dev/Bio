from Bio.PDB import PDBList, PDBParser
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Download PDB structure
pdb_id = "1A3N"

pdbl = PDBList()

pdbl.retrieve_pdb_file(
    pdb_id,
    pdir=".",
    file_format="pdb"
)

# Parse PDB file
parser = PDBParser(QUIET=True)

structure = parser.get_structure(
    pdb_id,
    f"pdb{pdb_id.lower()}.ent"
)

# Extract atomic coordinates
atoms = []

for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                atoms.append(atom.coord)

# Convert to NumPy array
atoms = np.array(atoms)

# Create 3D plot
fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(111, projection="3d")

# Plot atoms
ax.scatter(
    atoms[:, 0],
    atoms[:, 1],
    atoms[:, 2],
    c="blue",
    marker="o",
    s=10
)

# Labels and title
ax.set_title(f"3D Structure of {pdb_id}")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Display plot
plt.show()
