from qiskit import QuantumCircuit, Aer, execute, quantum_info 
from qiskit.visualization import plot_histogram , plot_state_qsphere,\
    plot_bloch_multivector, plot_bloch_vector
from qiskit.quantum_info import random_statevector 




# teleportation_circuit = qiskit.QuantumCircuit(q, c0, c1, c2)

# teleportation_circuit.h(q[1])
# teleportation_circuit.cx(q[1], q[2])

def teleporation(): #تلربورتيشن
    qc = QuantumCircuit(3,2)
    random_state= random_statevector([2])
    qc.initialize(random_state, 0)
    plot_bloch_multivector(random_state)#ستيت فكتور لسارا
 

    qc.h(1)
    qc.cx(1,2)
    qc.cx(0,1)
    qc.h(0)
    qc.barrier()
    qc.measure(0,0)
    qc.measure(1,1)
    qc.barrier()
    qc.x(2).c_if(1, 1)
    qc.z(2).c_if(0, 1)


    print(qc)

    job = execute(qc, Aer.get_backend('statevector_simulator'), shots=1)
    output= job.result().get_statevector()
    plot_state_qsphere(output)
    plot_bloch_multivector(output)



teleporation()