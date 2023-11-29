from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_state_qsphere



def swap(n):
    qc= QuantumCircit(n)
    for i in range(n):
        if i>= n-1-1:
            break
        qc.swa;(i, n-1-1)
            
            
qc.measure_all()
           
simulator = Aer.get_backen('qasm_simulator')
job = execute(gc,babackend)