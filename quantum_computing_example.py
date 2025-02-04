# quantum_computing_example.py

from qiskit import QuantumCircuit
from qiskit.compiler import execute
from qiskit.providers.basicaer import BasicAer
import matplotlib.pyplot as plt

# Cria um circuito quântico com 2 qubits e 2 bits clássicos
qc = QuantumCircuit(2, 2)
qc.h(0)            # Aplica a porta Hadamard no qubit 0 para criar superposição
qc.cx(0, 1)        # Aplica a porta CNOT para emaranhar os qubits
qc.measure([0, 1], [0, 1])  # Mede os qubits

# Exibe o circuito (opcional)
print(qc.draw())

# Usa o simulador básico (BasicAer)
backend = BasicAer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()

# Obtém os resultados das medições
counts = result.get_counts(qc)
print("Contagens:", counts)

# Plota um histograma dos resultados
plt.bar(counts.keys(), counts.values(), color='blue')
plt.xlabel('Resultado da Medição')
plt.ylabel('Contagens')
plt.title('Simulação com BasicAer')
plt.show()
