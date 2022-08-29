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

    if( "format" in extra_arguments and extra_arguments["format"] == "decimal" ):
        final_string = int(output, 2)
    elif( "format" in extra_arguments and extra_arguments["format"] == "hexadecimal" ):
        final_string = hex(int(output, 2))
    else:
        final_string = output

    return final_string
