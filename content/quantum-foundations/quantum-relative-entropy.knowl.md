+++
id = "quantum-foundations/quantum-relative-entropy"
title = "Quantum relative entropy"
kind = "knowl"
summary = "Noncommutative generalization of Kullback-Leibler divergence for density operators."
aliases = ["quantum-relative-entropy", "Quantum relative entropy"]
domains = ["quantum-foundations"]
prerequisites = ["quantum-foundations/density-operator", "quantum-foundations/spectrum-self-adjoint-finite"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "quantum-foundations/quantum-relative-entropy.md"
+++

Let \(\rho\) and \(\sigma\) be [[quantum-foundations/density-operator|density-operator]]s on a finite-dimensional Hilbert space \(H\). The **quantum relative entropy** (also called Umegaki relative entropy) is defined by
\[
D(\rho\|\sigma) :=
\begin{cases}
\operatorname{Tr}\!\big(\rho(\log\rho-\log\sigma)\big), & \text{if }\operatorname{supp}(\rho)\subseteq \operatorname{supp}(\sigma),\\[4pt]
+\infty, & \text{otherwise.}
\end{cases}
\]
The support condition is needed because \(\log\sigma\) is not finite on the kernel of \(\sigma\). The operators \(\log\rho\) and \(\log\sigma\) are defined by [[quantum-foundations/spectrum-self-adjoint-finite|spectral calculus]].

## Classical case

If \(\rho\) and \(\sigma\) commute, they are simultaneously diagonalizable and the formula reduces to the [[probability/relative-entropy-kl-divergence|Kullback–Leibler divergence]] of their eigenvalue distributions.

## Properties
- **Nonnegativity (Klein inequality):** \(D(\rho\|\sigma)\ge 0\), with equality iff \(\rho=\sigma\).
- **Not symmetric:** typically \(D(\rho\|\sigma)\ne D(\sigma\|\rho)\); it is not a metric.
- **Data processing inequality:** for any completely positive trace-preserving map \(\Phi\),
  \[
  D(\rho\|\sigma)\ \ge\ D(\Phi(\rho)\|\Phi(\sigma)).
  \]
  In particular, taking \(\Phi=\operatorname{Tr}_B\) (see [[quantum-foundations/partial-trace|partial trace]]) gives
  \[
  D(\rho_{AB}\|\sigma_{AB})\ \ge\ D(\rho_A\|\sigma_A),
  \quad \rho_A=\operatorname{Tr}_B(\rho_{AB}),\ \sigma_A=\operatorname{Tr}_B(\sigma_{AB}).
  \]

## Relation to von Neumann entropy
If \(d=\dim H\) and \(\tau=I/d\) is the maximally mixed state, then
\[
D(\rho\|\tau)=\log d - S(\rho),
\]
where \(S(\rho)\) is the [[quantum-foundations/von-neumann-entropy|von Neumann entropy]].
