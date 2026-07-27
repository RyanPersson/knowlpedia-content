+++
id = "stat-mech-quantum/quantum-partition-function"
title = "Quantum partition function"
kind = "knowl"
summary = "For a finite quantum system with Hamiltonian H, the canonical partition function is Tr(exp(-beta H))."
aliases = ["quantum-partition-function", "Quantum partition function"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/quantum-partition-function.md"
+++

Let \(H\) be a [[stat-mech-quantum/quantum-hamiltonian|Hamiltonian]] on a finite-dimensional Hilbert space and let \(\beta>0\). The **quantum partition function** is
\[
Z(\beta)=\operatorname{Tr}(e^{-\beta H}).
\]
If the eigenvalues of \(H\) are \(E_n\), counted with multiplicity, then \(Z(\beta)=\sum_ne^{-\beta E_n}\). It is finite and strictly positive.

## Derived quantities

The partition function normalizes the [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]] and determines the canonical free energy and mean energy:
\[
\rho_\beta=\frac{e^{-\beta H}}{Z(\beta)},
\qquad
F(\beta)=-\beta^{-1}\log Z(\beta),
\qquad
\langle H\rangle_\beta=-\frac{d}{d\beta}\log Z(\beta).
\]
Moreover,
\[
\frac{d^2}{d\beta^2}\log Z(\beta)
=\langle H^2\rangle_\beta-\langle H\rangle_\beta^2\ge0.
\]

## Independent systems

If \(\mathcal H=\mathcal H_A\otimes\mathcal H_B\) and
\(H=H_A\otimes I+I\otimes H_B\), then
\[
Z(\beta)=Z_A(\beta)Z_B(\beta).
\]
