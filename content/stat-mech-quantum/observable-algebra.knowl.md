+++
id = "stat-mech-quantum/observable-algebra"
title = "Observable algebra"
kind = "knowl"
summary = "A unital star-algebra of operators whose self-adjoint elements represent observables."
aliases = ["observable-algebra", "Observable algebra"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/observable-algebra.md"
prerequisites = ["linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal H\) be a finite-dimensional complex Hilbert space. An **observable algebra** is a unital \(*\)-subalgebra
\[
\mathcal A\subseteq \mathcal B(\mathcal H),
\]
where \(\mathcal B(\mathcal H)\) is the algebra of operators on \(\mathcal H\). Thus \(\mathcal A\) contains the identity and is closed under linear combinations, products, and adjoints. The physical observables are the self-adjoint elements of \(\mathcal A\).

## States

A state on \(\mathcal A\) is a positive normalized linear functional \(\omega:\mathcal A\to\mathbb C\):
\[
\omega(A^*A)\ge 0,
\qquad
\omega(I)=1.
\]
When \(\mathcal A=\mathcal B(\mathcal H)\), there is a unique [[quantum-foundations/density-operator|density operator]] \(\rho\) such that
\[
\omega(A)=\operatorname{Tr}(\rho A).
\]

## Remarks

Commutative observable algebras model compatible families of observables. Noncommutative algebras allow incompatible observables and are the natural setting for quantum dynamics and the [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]].
