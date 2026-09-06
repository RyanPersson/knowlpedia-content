+++
id = "stat-mech-quantum/quantum-expectation-value"
title = "Quantum expectation value"
kind = "knowl"
summary = "For a density operator and an observable, the expectation value is the trace of their product."
aliases = ["quantum-expectation-value", "Quantum expectation value"]
domains = ["stat-mech-quantum"]
prerequisites = ["quantum-foundations/density-operator", "stat-mech-quantum/observable-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "stat-mech-quantum/quantum-expectation-value.md"
+++

Let \(\rho\) be a [[quantum-foundations/density-operator|density operator]] on a finite-dimensional Hilbert space and \(A\) a self-adjoint element of the [[stat-mech-quantum/observable-algebra|observable algebra]]. The **expectation value** of \(A\) in the state \(\rho\) is
\[
\langle A\rangle_\rho=\operatorname{Tr}(\rho A).
\]
For a pure state \(\rho=|\psi\rangle\langle\psi|\), this is \(\langle A\rangle_\rho=\langle\psi|A|\psi\rangle\).

## Properties

The map \(A\mapsto\langle A\rangle_\rho\) is linear, positive, and normalized by \(\langle I\rangle_\rho=1\). For self-adjoint \(A\), its value is real and satisfies
\[
|\langle A\rangle_\rho|\le \|A\|.
\]
If \(P\) is an orthogonal projection, then \(\langle P\rangle_\rho\) is the Born probability of the outcome represented by \(P\).

## Thermal expectation

At inverse temperature \(\beta>0\), the thermal expectation is computed with the [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]] \(\rho_\beta\):
\[
\langle A\rangle_\beta=\operatorname{Tr}(\rho_\beta A).
\]
