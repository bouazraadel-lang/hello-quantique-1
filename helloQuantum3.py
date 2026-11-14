# 1. IMPORTS
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display

# 2. CRÉATION DU CIRCUIT
qc = QuantumCircuit(1, 1)  # 1 qubit, 1 bit classique

# 3. PORTE X (équivalent de NOT)
qc.x(0)

# 4. MESURE
qc.measure(0, 0)

# 5. AFFICHAGE DU CIRCUIT
print(qc)

# 6. SIMULATION
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)

result = job.result()
counts = result.get_counts()

# 7. AFFICHAGE DES RÉSULTATS
print("Résultats :", counts)

# 8. HISTOGRAMME
fig = plot_histogram(counts)
display(fig)
