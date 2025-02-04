from qiskit import QuantumCircuit
from qiskit.compiler import execute
from qiskit.providers.basicaer import BasicAer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Cria um circuito quântico simples com 2 qubits e 2 bits clássicos
qc = QuantumCircuit(2, 2)
qc.h(0)          # Aplica a porta Hadamard no primeiro qubit para criar superposição
qc.cx(0, 1)      # Aplica a porta CNOT para emaranhar os qubits
# Mede os qubits e armazena os resultados nos bits clássicos
qc.measure([0, 1], [0, 1])

# Usa o simulador QASM do BasicAer para executar o circuito
backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()

# Obtém as contagens dos resultados
counts = result.get_counts(qc)
print("Contagens:", counts)

# Plota o histograma dos resultados
plot_histogram(counts)
plt.show()
