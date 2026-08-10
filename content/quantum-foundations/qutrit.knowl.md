+++
id = "quantum-foundations/qutrit"
title = "Qutrit"
kind = "definition"
summary = "A three-level quantum system with state Hilbert space C^3."
aliases = ["quantum trit", "three-level quantum system"]
domains = ["quantum-foundations", "mathematical-physics"]
section_mode = "progressive"
+++

A **qutrit** is a quantum system whose state Hilbert space is three-dimensional over \(\mathbb C\), hence isomorphic after choosing an orthonormal basis to
\[
H\cong\mathbb C^3.
\]
Its pure states are rays in \(\mathbb C^3\), and its general states are positive trace-one operators \(\rho\in M_3(\mathbb C)\).

## Coordinates and observables

In a basis \(\{|0\rangle,|1\rangle,|2\rangle\}\), a normalized state vector is
\[
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle+\gamma|2\rangle,
\qquad
|\alpha|^2+|\beta|^2+|\gamma|^2=1,
\]
modulo a common phase. Thus the pure-state space is \(\mathbb{CP}^2\).

The observables are
\[
\mathfrak h_3(\mathbb C)=\{A\in M_3(\mathbb C):A^*=A\},
\]
a real Jordan algebra under \(A\circ B=\tfrac12(AB+BA)\); see the [[nonassociative-algebra/complex-qutrit-jordan-algebra|complex-qutrit Jordan algebra]].

## Comparison with a qubit

A qutrit has three basis levels rather than two. Its mixed-state space is not a Euclidean ball: the Bloch-ball description is special to two dimensions. A chosen two-dimensional subspace of \(\mathbb C^3\) determines an embedded [[quantum-foundations/qubit|qubit]], but no such subspace is canonical without extra data.

## “Octonionic qutrit” terminology

The [[nonassociative-algebra/exceptional-jordan-algebra|exceptional Jordan algebra]] \(\mathfrak h_3(\mathbb O)\) resembles \(\mathfrak h_3(\mathbb C)\) with octonionic entries and is informally called the observable algebra of an “octonionic qutrit.” This is an analogy about Euclidean Jordan algebras, not an ordinary complex-Hilbert-space qutrit.

## References

1. Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, tenth-anniversary edition, Cambridge University Press, 2010. [DOI record](https://doi.org/10.1017/CBO9780511976667). Relevant: finite-dimensional state spaces and density operators.
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv record](https://arxiv.org/abs/2606.15235). Relevant: §1.
