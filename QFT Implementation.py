import numpy as np
from qiskit import QuantumCircuit

n = 4
qft = QuantumCircuit(n, name="QFT")

for i in reversed(range(n)):                         #moves backwards through the Qbits, now without requiring negative indices in line 10
    qft.h(i)                                         #hadamard
    for j in range(i):
        qft.cp(np.pi / 2 ** (i - j), j, i)           #cROTATION phase gate

for k in range(n // 2):
    qft.swap(k, n - k - 1)

print(qft.draw())

#should my circuit instead run from q_3 to q_0, as it currently goes from q_0 to q_3 (top to bottom)?
#book seems to think the former
