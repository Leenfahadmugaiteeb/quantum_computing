from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_state_qsphere




qc = QuantumCircuit(2)

qc.h(0)

qc.cx(0, 1)

simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()


plot_state_qsphere(statevector)


