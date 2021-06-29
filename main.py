from qiskit import QuantumCircuit, Aer, execute, IBMQ

def run(input_data, solver_params, extra_arguments):

    size = int(input_data['size'])
    backend = Aer.get_backend('qasm_simulator')

    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()

    job = execute(qc, backend=backend, shots=size, memory=True)
    individual_shots = job.result().get_memory()

    output = ''
    for i in individual_shots:
        output+=i

    return output
