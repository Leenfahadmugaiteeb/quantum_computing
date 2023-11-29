from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.visualization import circuit_drawer

def prepare_entangled_qubits():
    qreg = QuantumRegister(2)
    circuit = QuantumCircuit(qreg)
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
        return QuantumCircuit(2)  # I gate |00> + |11>
    elif choice == 1:
        circuit = QuantumCircuit(2)
        circuit.x(1)
        return circuit  # X gate|10> + |01>
    elif choice == 2:
        circuit = QuantumCircuit(2)
        circuit.z(1)
        return circuit  # Z gate  |00> - |11>
    elif choice == 3:
        circuit = QuantumCircuit(2)
        circuit.z(1)
        circuit.x(1)
        return circuit  # ZX gate -|10> + |01>

def decode_message(sara_qubit, khalid_qubit, choice):
    circuit = encode_message(choice)
    
    
    
def send_entangled_qubits():
    circuit = prepare_entangled_qubits()
    backend = Aer.get_backend('statevector_simulator')
    job = execute(circuit, backend)
    result = job.result()
    statevector = result.get_statevector()
    sara_qubit = statevector
    khalid_qubit = statevector
    return sara_qubit, khalid_qubit, circuit
    


def superdense_coding_protocol():
    print("hello to the superdense coding protocol")
    choice = int(input("Choose a state (00, 01, 10, 11): "))
    sara_qubit, khalid_qubit, circuit = send_entangled_qubits()  
    result, decoding_circuit = decode_message(sara_qubit, khalid_qubit, choice)  
    print("Khalid received:", result)
    return circuit, decoding_circuit 

    circuit.barrier()
    circuit.cx(0, 1)
    circuit.h(0)
    circuit.barrier()
    circuit.measure([0, 1], [0, 1])

    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend)
    result = job.result()
    counts = result.get_counts()
    return counts, circuit

def superdense_coding_protocol():
    print("hello to the superdense coding protocol")
    choice = int(input("Choose a state (00, 10, 11, 01): "))
    sara_qubit, khalid_qubit = send_entangled_qubits()
    result, circuit = decode_message(sara_qubit, khalid_qubit, choice)
    print("Khalid received:", result)
    return circuit

final_circuit = superdense_coding_protocol()
circuit_drawer(final_circuit)