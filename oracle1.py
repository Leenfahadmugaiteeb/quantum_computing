import numpy as np
from qiskit import Aer, execute,QuantumCircuit



n = 8 #عدد الكيوبتس
qc = QuantumCircuit(n)
def oracle ():
    qc = QuantumCircuit(n+1)
    m = np.random.randint()
    if m==1:
        for i in range(n):
            qc.cx(i,n)
            
    return qc.to_instruction()


# def compile_circuit(function: QuantumCircuit):

#     n = function.num_qubits - 1
#     qc = QuantumCircuit(n + 1, n)
#     qc.x(n)
#     qc.h(range(n + 1))
#     qc.compose(function, inplace=True)
#     qc.h(range(n))
#     qc.measure(range(n), range(n))
#     return qc

# compile_circuit(
#     deutsch_function(3)
# ).draw()


# # سيركت لل القورذم 
def DJ_algorithm(n):
    qc= QuantumCircuit(n+1,n)
    qc.x(n)
    qc.h(range(n+1))
    
    qc.barrier()
    
    oracleF = oracle()
    qc=qc.compose((oracleF),[range(n+1)])
    
    qc.barrier()
    qc.h(range(n))
    qc.measure(range(n), range(n))
    
 #     رسم للسركت ديسبلاي
    qc.draw('mpl')
    
    job = execute(qc, Aer.get_backend('qasm_simulator'), shots=1)
    output = list(job.result().get_counts([0]))
    
    
    if '1' in output:
        print(f'{output}\nBalanced')
    else:
        print(f'{output}\nCostant')

DJ_algorithm(n)

