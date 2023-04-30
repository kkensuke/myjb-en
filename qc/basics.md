# Basics

## Quantum computer

A quantum computer is a computer that uses quantum mechanics to perform computations. Quantum computers are different from classical computers in that they use quantum bits, or qubits, instead of (classical) bits. A qubit is a two-level quantum mechanical system, which can be in a superposition of states. A classical bit, on the other hand, can only be in one of two states, 0 or 1. Moreover, quantum systems can have entanglement, which means that the state of one qubit can be correlated with the state of another qubit in a way that is not possible for classical systems. These properties of quantum systems might allow quantum computers to perform certain computations much faster than classical computers.


## What applications can quantum computers be used for?

Quantum computers can be used for a variety of applications, including:
- Quantum chemistry
- Machine learning
- Optimization
- Quantum simulation
- Encryption
- Search algorithms


## What is a qubit?

A qubit is a quantum mechanical system that can be in a superposition of states. A qubit can be in a state of 0 or 1, or in a superposition of both states. A qubit can be represented as a vector in a two-dimensional complex vector space. The state of $\ket{0}$ and $\ket{1}$ can be represented by the following vectors:

$$ \ket{0} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, $$
$$ \ket{1} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}. $$

And a general state, including superposition, of a qubit can be represented by a vector in the following form:

$$\begin{bmatrix} \alpha \\ \beta \end{bmatrix},\,\, |\alpha|^2 + |\beta|^2 = 1$$

where $\alpha$ and $\beta$ are complex numbers.


## What is a quantum gate?

Quantum gates are unitary transformations that act on a qubit. They are quantum analogues of classical logic gates and change the states of qubits. Quantum gates can be represented by matrices. The state of a qubit after a quantum gate is the product of the vector of the qubit and the matrix of the quantum gate. For example, the Hadamard gate is represented by the following matrix:

$$ H = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} $$

and $\ket{0}$ and $\ket{1}$ after the Hadamard gate are:

$$ \ket{0} \rightarrow \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ 1 \end{bmatrix} $$
$$ \ket{1} \rightarrow \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ -1 \end{bmatrix} $$


## What is a quantum circuit?

A quantum circuit is a series of quantum gates to perform a computation. A quantum circuit can also be represented by a matrix, which is the product of the matrices of the quantum gates in the circuit.


## Bloch sphere

The Bloch sphere is a three-dimensional representation of a qubit. A qubit can be represented by a vector in a two-dimensional complex vector space. The Bloch sphere is a three-dimensional representation of this vector. The Bloch sphere is a sphere with a radius of 1, centered at the origin.

$$ \ket{\psi} = \begin{bmatrix} \cos{\theta/2} \\ e^{i\phi}\sin{\theta/2} \end{bmatrix} $$


## What is entanglement?

Entanglement is a quantum phenomenon where two qubits interact with each other and become linked such that they can no longer be described independently of each other. They become entangled, meaning that the quantum state of one particle is dependent upon the quantum state of the other, no matter how far apart they are. Entanglement is one of the most fascinating and mysterious principles of quantum mechanics, as it allows for information to be transferred instantaneously between entangled particles, even at opposite ends of the universe, which is not possible in classical physics.