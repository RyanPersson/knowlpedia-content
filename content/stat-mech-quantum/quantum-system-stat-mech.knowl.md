+++
id = "stat-mech-quantum/quantum-system-stat-mech"
title = "Finite quantum statistical system"
kind = "knowl"
summary = "A finite-dimensional Hilbert space with an observable algebra and a self-adjoint Hamiltonian."
aliases = ["quantum-system-stat-mech", "Finite quantum statistical system"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/quantum-system-stat-mech.md"
+++

A **finite quantum statistical system** consists of a triple \((\mathcal H,\mathcal A,H)\), where \(\mathcal H\) is a finite-dimensional complex Hilbert space, \(\mathcal A\subseteq\mathcal B(\mathcal H)\) is a unital [[stat-mech-quantum/observable-algebra|observable algebra]], and \(H=H^*\in\mathcal A\) is the [[stat-mech-quantum/quantum-hamiltonian|Hamiltonian]]. A state is a positive normalized functional on \(\mathcal A\); on \(\mathcal B(\mathcal H)\) it is represented uniquely by a [[quantum-foundations/density-operator|density operator]].

## Dynamics and equilibrium

The Hamiltonian generates the dynamics
\[
\tau_t(A)=e^{itH/\hbar}Ae^{-itH/\hbar}.
\]
For each inverse temperature \(\beta>0\), it also determines the [[stat-mech-quantum/quantum-partition-function|partition function]] and [[stat-mech-quantum/gibbs-state-quantum|Gibbs state]].

## Scope

This finite-dimensional model avoids the domain and trace-class issues that arise for unbounded Hamiltonians or infinite systems. Those settings require additional analytic hypotheses and, for equilibrium, the operator-algebraic KMS formulation.
