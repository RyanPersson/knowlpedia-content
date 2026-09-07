+++
id = "quantum-foundations/density-operator"
title = "Density Operator"
kind = "knowl"
summary = "A positive semidefinite trace-one operator representing the state of a quantum system, allowing both pure and statistical mixtures."
aliases = ["density-operator", "Density Operator"]
domains = ["quantum-foundations"]
legacy_source_path = "quantum-foundations/density-operator.md"
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/trace-class-operator", "quantum-foundations/trace-operator", "quantum-foundations/positive-semidefinite-operator"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

Let \(H\) be a complex [[linear-algebra/hilbert-space|Hilbert space]]. A **density operator** (also called a **density matrix**) is a positive [[functional-analysis/trace-class-operator|trace-class]] operator \(\rho:H\to H\) such that:

1. **Positivity:** \(\rho \ge 0\), meaning \(\langle \psi,\rho\psi\rangle \ge 0\) for all \(\psi\in H\).
2. **Unit trace:** \(\operatorname{Tr}(\rho)=1\), where \(\operatorname{Tr}\) is the operator trace ([[quantum-foundations/trace-operator|Trace Operator]]).

In finite dimension, trace-class is automatic, so these conditions say that \(\rho\) is a positive semidefinite matrix of trace one.

## Basic structural facts (finite dimension)
- \(\rho\) is automatically self-adjoint: \(\rho=\rho^\ast\).
- All eigenvalues of \(\rho\) are real and lie in \([0,1]\).
- The eigenvalues sum to \(1\): if \(\rho\) has eigenvalues \((p_i)\), then \(\sum_i p_i=1\).

Thus \(\rho\) admits a spectral decomposition
\[
\rho = \sum_i p_i\,|\phi_i\rangle\langle \phi_i|,
\]
with \((\phi_i)\) orthonormal and \(p_i\ge 0\), \(\sum_i p_i=1\).

## Pure vs mixed
- \(\rho\) is a **pure state** iff it has rank \(1\), equivalently iff \(\rho^2=\rho\), equivalently iff \(\operatorname{Tr}(\rho^2)=1\). (See [[quantum-foundations/pure-state-quantum|Pure State Quantum]].)
- Otherwise \(\rho\) is **mixed** and can be written as a possibly countable mixture (a finite [[convex-analysis/convex-combination|convex combination]] in finite dimension) \(\rho=\sum_k q_k |\psi_k\rangle\langle\psi_k|\) with \(q_k\ge 0\), \(\sum_k q_k=1\). The sum converges in trace norm. (See [[quantum-foundations/mixed-state-quantum|Mixed State Quantum]].)

## Expectation values (Born rule in operator form)
If \(A\) is a bounded observable (a self-adjoint operator, see [[quantum-foundations/self-adjoint-operator-observable|Self Adjoint Operator Observable]]), then the expectation value in state \(\rho\) is
\[
\mathbb{E}_\rho[A] = \operatorname{Tr}(\rho A).
\]
This formula unifies pure and mixed states. For an unbounded observable, its expectation requires additional spectral-integrability and domain conditions.

## Dynamics and transformations (finite dimension)
- **Unitary evolution:** if \(U\) is unitary, then \(\rho\) evolves as \(\rho \mapsto U\rho U^\ast\).
- **Projective measurement:** spectral projectors \(P_i\) (as in [[quantum-foundations/spectrum-self-adjoint-finite|Spectrum Self Adjoint Finite]]) define outcome probabilities \(\Pr(i)=\operatorname{Tr}(\rho P_i)\).

## Information-theoretic quantities
Two common functionals of \(\rho\) are:

- Von Neumann entropy: \(S(\rho) = -\operatorname{Tr}(\rho\log\rho)\) (see [[quantum-foundations/von-neumann-entropy|Von Neumann Entropy]]).
- Relative entropy: \(D(\rho\|\sigma)=\operatorname{Tr}(\rho(\log\rho-\log\sigma))\) under suitable support conditions (see [[quantum-foundations/quantum-relative-entropy|Quantum Relative Entropy]]).
In infinite dimension these entropy quantities can be \(+\infty\); the logarithmic expressions require their spectral interpretation, not an assumption that every displayed product is trace-class.
