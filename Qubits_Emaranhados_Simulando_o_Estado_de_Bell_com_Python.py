from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit.providers.aer import AerSimulator  # Import AerSimulator
import matplotlib.pyplot as plt

def quantum_bell_state():
    """
    Cria e simula um estado de Bell usando Qiskit sem BasicAer.
    """

    print("Simulação Quântica - Estado de Bell\n")

    # Cria um circuito quântico com 2 qubits e 2 bits clássicos.
    qc = QuantumCircuit(2, 2)

    # Cria um estado de Bell:
    qc.h(0)  # Aplica a porta Hadamard no qubit 0 para criar superposição.
    qc.cx(0, 1)  # Aplica a porta CNOT para emaranhar os qubits.

    # Mede os qubits.
    qc.measure([0, 1], [0, 1])

    # Exibe o desenho do circuito.
    print("Circuito Quântico:")
    print(qc.draw(output="text"))

    # Configura o simulador.
    backend = AerSimulator()  

    # Transpila e executa o circuito.
    compiled_circuit = transpile(qc, backend)
    result = backend.run(compiled_circuit, shots=1024).result() 
    counts = result.get_counts() 

    # Exibe os resultados corretamente
    print("Resultados da Simulação:")
    print(counts)

    # Plota o histograma dos resultados
    plot_histogram(counts)
    plt.show()

# Chama a função para rodar a simulação.
quantum_bell_state()
