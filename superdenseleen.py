from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister,\
    Aer,BasicAer,execute

from qiskit.visualization import plot_histogram, plot_state_qsphere, plot_bloch_multivector
from qiskit.quantum_info import random_statevector
from qiskit.extensions import Initialize

qr = QuantumRegister(3,name = 'qr')
c1 = ClassicalRegister(1,name = 'c1')
c2 = ClassicalRegister(1,name = 'c2')

qc = QuantumCircuit(qr,c1,c2)

vec=random_statevector(2)
init_gate = Initialize(vec)
init_gate.label = 'init'

plot_bloch_multivector(init_gate)

qc.append(init_gate, [0])

qc.barrier()
qc.h(1)
qc.cx(1,2)
qc.cx(0,1)
qc.h(0)
qc.barrier()
qc.measure([0,1], [c1[0], c2[0]])

with qc.if_test((c1[0], 1)):
    qc.x(2)
with qc.if_test((c2[0], 1)):
    qc.z(2)
    
qc.draw('mpl')
job2 = execute(qc, Aer.backend('statevector_simulator'), shots=1024)
output2= job2.result().get_statevector()
plot_bloch_multivector(output2)

qc1 = QuantumCircuit(2,1)
qc1.x(0)
qc2=QuantumCircuit(2,1)
qc2.cx(0,1)
qc2.z(1)

qc = QuantumCircuit()
qc = qc1.compose(qc2)

print(qc)