import random
from qiskit import QuantumCircuit, Aer, execute 


# الكيوبتس 
n = int(input('n = '))
qc = QuantumCircuit(n+1,n)
def oracle():
    oracle = QuantumCircuit(n+1, name='Oracle')
    state = ['Balanced', 'Constant']
    rand = random.choice(state)  
    if rand == 'Balanced': 
        for i in range(n):
            oracle.cx(i, n)
    oracle.draw("mpl")
    return oracle.to_instruction()

# سوبر بوزيشن
def hedamart():
    for i in range(n):
        qc.h(i)



# def DJ_algorithm(n):
#     qc= QuantumCircuit(n+1,n)
#     qc.x(n)
#     qc.h(range(n+1))
    
#     qc.barrier()
# result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1).result()
# counts = list(result.get_counts())[0]

qc.x(n)
qc.h(n)
hedamart()
# بارير
qc.barrier()

  

#استدعاء الاوركل
oracle = oracle()
qc = qc.compose(oracle)
qc.barrier()

hedamart()
qc.barrier()

# مجرمنت
for i in range(n):
    qc.measure(i, i)
rslt = execute(qc,Aer.get_backend('qasm_simulator'), shots=1)
c = list(rslt.result().get_counts())[0] 
print(c)
if '0' in c:
    print('oracle is constant')
else: print('oracle is balanced')
    
# الفاينل سركت مرسومه
qc.draw("mpl")