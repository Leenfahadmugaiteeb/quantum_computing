from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

def prepare_entangled_qubits():
    qreg = QuantumRegister(2)
    creg = ClassicalRegister(2)
    circuit = QuantumCircuit(qreg, creg)
    circuit.h(qreg[0])
    circuit.cx(qreg[0], qreg[1])
    return circuit

def send_entangled_qubits():
    circuit = prepare_entangled_qubits()
    backend = Aer.get_backend('statevector_simulator')
    job = execute(circuit, backend)
    result = job.result()
    statevector = result.get_statevector()
    sara_qubit = statevector
    khalid_qubit = statevector
    return sara_qubit, khalid_qubit


def encode_message(choice):
    if choice == 0:
        return QuantumCircuit(2, 2)  # I gate, resulting state = |00> + |11>
    elif choice == 1:
        circuit = QuantumCircuit(2, 2)
        circuit.x(1)
        return circuit  # X gate, resulting state = |10> + |01>
    elif choice == 2:
        circuit = QuantumCircuit(2, 2)
        circuit.z(1)
        return circuit  # Z gate, resulting state = |00> - |11>
    elif choice == 3:
        circuit = QuantumCircuit(2, 2)
        circuit.z(1)
        circuit.x(1)
        return circuit  # ZX gate, resulting state = -|10> + |01>

def decode_message(sara_qubit, khalid_qubit, choice):
    circuit = encode_message(choice)

    circuit.barrier()
    circuit.cx(0, 1)
    circuit.h(0)
    circuit.barrier()
    circuit.measure([0, 1], [0, 1])

    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend)
    result = job.result()
    counts = result.get_counts()
    return counts

def superdense_coding_protocol():
    print("Welcome to the Superdense Coding Protocol")
    choice = int(input("Choose a state (0, 1, 2, 3): "))
    sara_qubit, khalid_qubit = send_entangled_qubits()
    result = decode_message(sara_qubit, khalid_qubit, choice)
    print("Khalid received:", result)

superdense_coding_protocol()
