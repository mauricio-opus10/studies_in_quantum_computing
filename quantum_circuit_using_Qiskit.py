from qiskit import QuantumCircuit, transpile, assemble
from qiskit.providers.aer import AerSimulator
import matplotlib.pyplot as plt

# Criando um circuito quântico com 2 qubits
qc = QuantumCircuit(2)
qc.h(0)  # Aplicando a porta Hadamard no primeiro qubit para criar superposição
qc.cx(0, 1)  # Aplicando a porta CNOT para criar emaranhamento entre os qubits

# Desenhando o circuito para visualização
qc.draw(output='mpl')
plt.show()

# Criando o simulador Aer
simulator = AerSimulator()

# Transpilando o circuito para ser compatível com o backend do simulador
compiled_circuit = transpile(qc, simulator)

# Executando o circuito no simulador
job = simulator.run(compiled_circuit)
result = job.result()

# Obtendo os dados da simulação
print("Resultado da simulação:", result)
