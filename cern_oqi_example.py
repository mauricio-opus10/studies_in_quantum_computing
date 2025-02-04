"""
Exemplo de Código de Computação Quântica inspirado no CERN e no Open Quantum Institute (OQI).
Este exemplo cria um estado de Bell usando Qiskit, simula-o e plota os resultados.
"""

from qiskit import QuantumCircuit, transpile, assemble
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def main():
    # Cabeçalho informativo
    print("CERN - Open Quantum Institute (OQI) - Exemplo de Simulação Quântica\n")

    # Cria um circuito quântico com 2 qubits e 2 bits clássicos
    qc = QuantumCircuit(2, 2)

    # Cria um estado de Bell:
    # 1. Coloca o primeiro qubit em superposição com a porta Hadamard.
    # 2. Emaranha o primeiro e o segundo qubit com a porta CNOT.
    qc.h(0)
    qc.cx(0, 1)

    # Mede os dois qubits
    qc.measure([0, 1], [0, 1])

    # Exibe o desenho do circuito
    print("Circuito Quântico:")
    print(qc.draw(output="text"))

    # Configura o simulador Aer
    simulator = AerSimulator()

    # Transpila o circuito para o backend escolhido
    compiled_circuit = transpile(qc, simulator)

    # Monta o objeto de execução com 1024 "shots" (execuções)
    qobj = assemble(compiled_circuit, shots=1024)

    # Executa a simulação e coleta o resultado
    result = simulator.run(qobj).result()
    counts = result.get_counts(qc)

    # Exibe os resultados no terminal
    print("\nResultados da Simulação (Contagens):")
    print(counts)

    # Plota um histograma dos resultados
    plot_histogram(counts)
    plt.title("Resultados da Simulação - Estado de Bell")
    plt.show()


if __name__ == '__main__':
    main()
