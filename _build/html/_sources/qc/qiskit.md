# Qiskit

## Installation

At first, we make a virtual environment for this test project.

```bash
python3 -m venv qiskit
```

Then, we activate the virtual environment.

```bash
source qiskit/bin/activate
```

Lastly, we install Qiskit.

```bash
pip install qiskit
```

To implement Qiskit on Jupyter Notebook, we also install the following useful packages.

```bash
pip install matplotlib
pip install jupyter
```


## Basics

### Make a quantum circuit

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
```

`QuantumCircuit` is a class to make a quantum circuit. The argument `2` means that the quantum circuit has two qubits. The qubits indeces are numbered from 0.

### Add a quantum gate

Generated quantum circuit is empty. We add a quantum gate to the quantum circuit to generate a Bell state.

```python
qc.h(0)
qc.cx(0, 1)
```

### Draw a quantum circuit

```python
qc.draw(output='mpl')
```

### Show the state vector on the bloch sphere

```python
from qiskit.visualization import plot_bloch_multivector

plot_bloch_multivector(qc)
```

### Add a measurement

To extract information from a quantum circuit, we need to perform measurements.

```python
qc.measure_all()
```

### Simulate the quantum circuit

```python
from qiskit import Aer, execute

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend).result()
counts = result.get_counts(qc)
print(counts)
```

### Visualize the result



```python
from qiskit.visualization import plot_histogram

plot_histogram(counts)
```

## Reference

- [Qiskit](https://qiskit.org/)