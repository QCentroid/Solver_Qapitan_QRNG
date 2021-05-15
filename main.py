from qiskit import QuantumCircuit, Aer, execute, IBMQ


def run(input_data, solver_params = False, extra_agruments):
    
    size = int(input_data['data']['size'])

    if(input_data['provider'] == 'simulator'):
        backend = Aer.get_backend('qasm_simulator')
        #backend = provider.get_backend('ibmq_qasm_simulator')
    else:
        IBMQ.load_account()
        provider = IBMQ.get_provider()
        backend = provider.get_backend('ibmq_qasm_simulator')


    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()

    job = execute(qc, backend=backend, shots=size, memory=True)
    individual_shots = job.result().get_memory()

    output = ''
    for i in individual_shots:
        output+=i

    return output