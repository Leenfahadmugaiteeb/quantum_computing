from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# Step 1: Alice chooses a string of random bits and bases
np.random.seed(0)  # For reproducibility
n = 8  # Number of qubits
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.choice(['X', 'Z'], size=n)

# Step 2: Alice encodes each bit onto a qubit using the chosen basis
alice_circuit = QuantumCircuit(n, n)
for i in range(n):
    if alice_bases[i] == 'X':
        if alice_bits[i] == 1:
            alice_circuit.h(i)
    elif alice_bases[i] == 'Z':
        if alice_bits[i] == 1:
            alice_circuit.z(i)
alice_circuit.barrier()

# Step 3: Bob measures each qubit at random
bob_bases = np.random.choice(['X', 'Z'], size=n)
bob_circuit = QuantumCircuit(n, n)
for i in range(n):
    if bob_bases[i] == 'X':
        bob_circuit.h(i)
    bob_circuit.measure(i, i)

# Combine Alice and Bob's circuits
bb84_circuit = alice_circuit + bob_circuit

# Execute the combined circuit
backend = Aer.get_backend('qasm_simulator')
counts = execute(bb84_circuit, backend, shots=1).result().get_counts()

# Extract Alice and Bob's measurement results
alice_results = {k[::-1]: v for k, v in counts.items() if k[0] == '0'}
bob_results = {k[::-1]: v for k, v in counts.items() if k[0] == '1'}

# Compare Alice and Bob's bases and generate the shared key
shared_key = [alice_bit for i, alice_bit in enumerate(alice_bits) if alice_bases[i] == bob_bases[i]]
matched_sample = [index for index in alice_results.keys() if index in bob_results]

# Visualize the combined circuit
bb84_circuit.draw(output='mpl')

# Display the shared key and matched sample
print("Shared Key:", shared_key)
print("Matched Sample of Keys:", matched_sample)
if shared_key == matched_sample:
    print("Successful transmission - No eavesdropper detected!")
else:
    print("Potential eavesdropper detected!")