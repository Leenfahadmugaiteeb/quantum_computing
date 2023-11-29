from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import numpy as np

def create_entangled_state():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit

def superdense_coding(message):
    circuit = QuantumCircuit(2)
    
    if message == 00:
        pass
    elif message == 10:
        circuit.x(0)
    elif message == 11:
        circuit.z(0)
    elif message == 1:
        circuit.z(0)
        circuit.x(0)
        
    circuit.cx(0, 1)
    circuit.h(0)
    return circuit

message = int(input("Enter (00, 01, 10, 11): "))

entangled_state = create_entangled_state()

superdense_circuit = superdense_coding(message)


backend = Aer.get_backend('statevector_simulator')
result = execute(superdense_circuit, backend).result()
statevector = result.get_statevector()
print("Output statevector:", statevector)


superdense_circuit.draw(output='mpl')