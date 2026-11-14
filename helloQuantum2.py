# 1. IMPORTS
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display

# 2. CRÉATION DU CIRCUIT
qc = QuantumCircuit(1, 1)

# 3. MESURE (aucune porte appliquée)
qc.measure(0, 0)

# 4. AFFICHAGE DU CIRCUIT
print(qc)

# 5. SIMULATION
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)

# 6. RÉSULTATS
result = job.result()
counts = result.get_counts()
print("Résultats :", counts)

# 7. HISTOGRAMME
fig = plot_histogram(counts)
display(fig))
