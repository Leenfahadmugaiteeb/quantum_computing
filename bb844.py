from qiskit import QuantumCircuit, Aer, execute
import numpy as np
# اليس تختار راندوم بتس و بيسيز

np.random.seed(0)  # reproducibilityلل

n = 8  #رقم الكيوبتس
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.choice(['X', 'Z'], size=n)
# اليس انكود كل بيت لكيوبت باستخدام البيس الي اختارته 
alice_circuit = QuantumCircuit(n, n)
for i in range(n):
    if alice_bases[i] == 'X':
        if alice_bits[i] == 1:
            alice_circuit.h(i)
    elif alice_bases[i] == 'Z':
        if alice_bits[i] == 1:
            alice_circuit.z(i)
alice_circuit.barrier()
# بوب يسوي مجرمنت لكل كيوبت في راندوم
bob_bases = np.random.choice(['X', 'Z'], size=n)
bob_circuit = QuantumCircuit(n, n)
for i in range(n):
    if bob_bases[i] == 'X':
        bob_circuit.h(i)
    bob_circuit.measure(i, i)

# كومباين سيركتس اليس و بوب
bb84_circuit = alice_circuit + bob_circuit

# اكسكيوت للكومبايند سركتس
backend = Aer.get_backend('qasm_simulator')
counts = execute(bb84_circuit, backend, shots=1).result().get_counts()

# استخلاص نتائج مجرمنت اليس وبوب
alice_results = {k[::-1]: v for k, v in counts.items() if k[0] == '0'}
bob_results = {k[::-1]: v for k, v in counts.items() if k[0] == '1'}

# مقارنة الشيرد كي
shared_key = []
matched_sample = []
for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        shared_key.append(alice_bits[i])
        if alice_results.get(format(i, '03b')) is not None and bob_results.get(format(i, '03b')) is not None:
            matched_sample.append(alice_bits[i])

bb84_circuit.draw(output='mpl')

# دسبلاي للماتشد كي والسامبل
print("Shared Key:", shared_key)
print("Matched Sample of Keys:", matched_sample)
if shared_key == matched_sample:
    print("successful transmission no eavesdropper detected")
else:
    print("eavesdropper detected")