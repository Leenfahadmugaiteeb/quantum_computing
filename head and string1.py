import random
from qiskit import QuantumCircuit, Aer, execute 

# Input value n
n = int(input('n = '))

# Create quantum circuit with n+1 qubits and n classical bits
qc = QuantumCircuit(n+1,n)

# Define the oracle
def oracle():
    oracle_circuit = QuantumCircuit(n+1, name='Oracle')
    state = ['Balanced', 'Constant']
    rand = random.choice(state)  
    if rand == 'Balanced': 
        for i in range(n):
            oracle_circuit.cx(i, n)
    return oracle_circuit.to_instruction()

# Apply Hadamard gate to each qubit
def hadamart():
    for i in range(n):
        qc.h(i)

# Apply X gate to the last qubit and then apply Hadamard gate to it
qc.x(n)
qc.h(n)
hadamart()
qc.barrier()

# Call the Oracle
oracle_inst = oracle()
qc.append(oracle_inst, list(range(n+1)))
qc.barrier()

# Apply Hadamard gate to each qubit again
hadamart()
qc.barrier()

# Measurement
for i in range(n):
    qc.measure(i, i)

# Run the quantum circuit on the qasm simulator
result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1).result()
counts = list(result.get_counts())[0]

# Check the output for constant or balanced function
if '0' in counts:
    print('Oracle is Constant')
else:
    print('Oracle is Balanced')
    
print(counts)
qc.draw("mpl")