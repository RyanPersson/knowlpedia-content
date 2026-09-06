+++
id = "stat-mech-quantum/kms-condition-finite"
title = "KMS condition in finite quantum systems"
kind = "knowl"
summary = "An analytic boundary condition on equilibrium correlation functions at inverse temperature beta."
aliases = ["kms-condition-finite", "KMS condition in finite quantum systems"]
domains = ["stat-mech-quantum"]
prerequisites = ["stat-mech-quantum/quantum-hamiltonian", "stat-mech-quantum/observable-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "stat-mech-quantum/kms-condition-finite.md"
+++

Let \(\mathcal A=\mathcal B(\mathcal H)\) for a finite-dimensional Hilbert space, let \(H=H^*\), fix \(\beta>0\), and use units with \(\hbar=1\). Write
\[
\tau_t(A)=e^{itH}Ae^{-itH}.
\]
A state \(\omega\) satisfies the **\(\beta\)-KMS condition** if, for every \(A,B\in\mathcal A\), there is a function \(F_{A,B}\) continuous on \(0\le\operatorname{Im}z\le\beta\), analytic in its interior, and satisfying
\[
F_{A,B}(t)=\omega(A\tau_t(B)),
\qquad
F_{A,B}(t+i\beta)=\omega(\tau_t(B)A)
\]
for every \(t\in\mathbb R\).

## Finite-dimensional characterization

The [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]]
\[
\omega_\beta(A)=\frac{\operatorname{Tr}(e^{-\beta H}A)}{\operatorname{Tr}(e^{-\beta H})}
\]
satisfies the \(\beta\)-KMS condition. Conversely, on the full matrix algebra it is the unique \(\beta\)-KMS state for \(\tau\).

## Remarks

Every KMS state is invariant under the dynamics. The condition is formulated in terms of the observable algebra and time evolution, so it extends to infinite systems where a trace-class Gibbs density operator need not exist.
