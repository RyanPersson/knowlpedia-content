+++
id = "quantum-foundations/qubit"
title = "Qubit"
kind = "definition"
summary = "A two-level quantum system with state Hilbert space C^2."
aliases = ["quantum bit", "two-level quantum system"]
domains = ["quantum-foundations", "mathematical-physics"]
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/orthonormal-basis"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **qubit** is a quantum system whose state [[linear-algebra/hilbert-space|Hilbert space]] is two-dimensional over \(\mathbb C\), hence isomorphic after choosing an [[linear-algebra/orthonormal-basis|orthonormal basis]] to
\[
H\cong\mathbb C^2.
\]
A pure state is a ray in \(H\), equivalently a rank-one density operator, and a general state is a positive trace-one operator \(\rho\in M_2(\mathbb C)\).

## States and observables

After choosing \(\{|0\rangle,|1\rangle\}\), a [[quantum-foundations/normalized-state-vector|normalized state vector]] is
\[
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\qquad |\alpha|^2+|\beta|^2=1,
\]
with vectors differing by global phase representing the same [[quantum-foundations/pure-state-quantum|pure state]]. Mixed states are [[quantum-foundations/density-operator|density operators]].

The observables are the self-adjoint matrices
\[
\mathfrak h_2(\mathbb C)=\{A\in M_2(\mathbb C):A^*=A\}.
\]
With \(A\circ B=\tfrac12(AB+BA)\), they form the [[nonassociative-algebra/complex-qubit-jordan-algebra|complex-qubit Jordan algebra]].

## Bloch-ball picture

Every density operator is uniquely
\[
\rho=\tfrac12(I+\mathbf r\cdot\boldsymbol\sigma),
\qquad \mathbf r\in\mathbb R^3,\quad \|\mathbf r\|\le1.
\]
Pure states form the boundary sphere; mixed states fill the ball.

## Relation to the \(F_4\) construction

In the \(F_4\) stabilizer characterization of the [[mathematical-physics/standard-model-gauge-group|Standard Model group]], a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] \(X\cong\mathfrak h_2(\mathbb C)\) is interpreted as the observable algebra of a qubit inside a qutrit observable algebra \(B\cong\mathfrak h_3(\mathbb C)\).

## References

1. Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, tenth-anniversary edition, Cambridge University Press, 2010. [DOI record](https://doi.org/10.1017/CBO9780511976667). Relevant: §§1.2 and 2.2.
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv record](https://arxiv.org/abs/2606.15235). Relevant: §1.
