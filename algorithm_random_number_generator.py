from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def quantum_random_bit() -> int:
    quantum_circuit = QuantumCircuit(1,1)


    quantum_circuit.h(0)

    quantum_circuit.measure(0,0)

    simulator = AerSimulator()
    job = simulator.run(quantum_circuit,shots = 1000)
    result = job.result()
    counts = result.get_counts()

    return int(list(counts.keys())[0])

def quantum_random_number (n_bits: int = 8) -> int:
    bits = [quantum_random_bit() for i in range(n_bits)]

    binary_string = ''.join(str(b) for b in bits)
    return int(binary_string, 2)

print("bits aleatórios")
for i in range(10):
    print(quantum_random_bit(), end ="")

print(f"\n\nNúmero aleatório de 8 bits (0-255): {quantum_random_number(8)}")
print(f"Número aleatório de 16 bits (0-65535): {quantum_random_number(16)}")

qc = QuantumCircuit(3, 3)
qc.h(range(3))
qc.measure(range(3), range(3))

print(qc.draw('text'))