
import math

import numpy as np
import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def quantum_fourier_transform(number_of_qubits: int = 3) -> qiskit.result.counts.Counts:
    if isinstance(number_of_qubits, str):
        raise TypeError("number of qubits must be a integer.")
    if number_of_qubits <= 0:
        raise ValueError("number of qubits must be > 0.")
    if math.floor(number_of_qubits) != number_of_qubits:
        raise ValueError("number of qubits must be exact integer.")
    if number_of_qubits > 10:
        raise ValueError("number of qubits too large to simulate(>10).")

    qr = QuantumRegister(number_of_qubits, "qr")
    cr = ClassicalRegister(number_of_qubits, "cr")

    quantum_circuit = QuantumCircuit(qr, cr)

    counter = number_of_qubits

    for i in range(counter):
        quantum_circuit.h(number_of_qubits - i - 1)
        counter -= 1
        for j in range(counter):
            quantum_circuit.cp(np.pi / 2 ** (counter - j), j, counter)

    for k in range(number_of_qubits // 2):
        quantum_circuit.swap(k, number_of_qubits - k - 1)

    
    quantum_circuit.measure(qr, cr)
    
    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=10000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(
        f"Total count for quantum fourier transform state is: \
    {quantum_fourier_transform(3)}"
    )
