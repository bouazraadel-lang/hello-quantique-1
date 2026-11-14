# 1. IMPORTS
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 2. CRÉATION DU CIRCUIT
qc = QuantumCircuit(1, 1)  # 1 qubit, 1 bit classique

# 3. PORTE HADAMARD
qc.h(0)

# 4. MESURE
qc.measure(0, 0)

# Affichage du circuit (texte)
print(qc)

# 5. SIMULATION
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)

result = job.result()
counts = result.get_counts()

# 6. AFFICHAGE
print(counts)
plot_histogram(counts)
