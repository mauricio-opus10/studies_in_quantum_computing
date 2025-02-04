#Simulando um Estado de Bell

from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import AerSimulator  
import matplotlib.pyplot as plt

def quantum_bell_state():
    """
    Simula um Estado de Bell utilizando Qiskit.
    """

    print("🔹 Simulando um Estado de Bell...\n")

    # Criação do circuito quântico com 2 qubits e 2 bits clássicos.
    qc = QuantumCircuit(2, 2)

    # Aplicação da porta Hadamard para criar superposição.
    qc.h(0)  

    # Aplicação da porta CNOT para emaranhar os qubits.
    qc.cx(0, 1)  

    # Medida dos qubits
    qc.measure([0, 1], [0, 1])

    # Exibe o circuito
    print(qc.draw(output="text"))

    # Configuração do simulador quântico
    backend = AerSimulator()  
    compiled_circuit = transpile(qc, backend)
    result = backend.run(compiled_circuit, shots=1024).result() 
    counts = result.get_counts() 

    # Exibe os resultados
    print("\n🔹 Resultados da Simulação:")
    print(counts)

    # Plota o histograma dos estados medidos
    plot_histogram(counts)
    plt.show()

# Rodando a simulação
quantum_bell_state()

