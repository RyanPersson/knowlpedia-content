+++
id = "mathematical-physics/standard-model-fermion-generation"
title = "Standard Model fermion generation"
kind = "definition"
summary = "One repeated family of quark and lepton multiplets with the same internal gauge quantum numbers."
aliases = ["fermion generation", "Standard Model family", "one generation of fermions"]
domains = ["mathematical-physics"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

A **Standard Model fermion generation** is one copy of the quark and lepton multiplets carrying the following representations of \(SU(2)_L\times SU(3)_C\times U(1)_Y\):
\[
\begin{array}{c|c}
\text{field}&(SU(2),SU(3))_Y\\ \hline
Q_L&(2,3)_{1/3}\\
L_L&(2,1)_{-1}\\
u_R&(1,3)_{4/3}\\
d_R&(1,3)_{-2/3}\\
e_R&(1,1)_{-2}\\
\nu_R&(1,1)_0\quad\text{if included.}
\end{array}
\]
Here \(Q=T_3+Y/2\). The minimal Standard Model omits \(\nu_R\); adjoining it gives \(16\) complex internal Weyl species in a generation. Antiparticles transform in the dual representations.

## Left-handed Weyl convention

One may describe every field as left-handed by replacing right-handed fields with their charge conjugates. The same generation is then
\[
(2,3)_{1/3}\oplus(2,1)_{-1}\oplus
(1,\bar 3)_{-4/3}\oplus(1,\bar 3)_{2/3}\oplus
(1,1)_2\oplus(1,1)_0.
\]
Mixing this convention with the right-handed-field convention conjugates some color representations and reverses their hypercharges.

## What “generation” records

The three observed generations have the same gauge representations but different masses and flavor-mixing data. The representation above records only internal gauge quantum numbers; it excludes momentum, spinor components, Yukawa couplings, and empirical flavor labels.

## Exterior-algebra packaging

Including \(\nu_R\), one generation plus its antiparticles is a \(32\)-dimensional representation isomorphic to [[mathematical-physics/standard-model-exterior-algebra-representation|\(\Lambda\mathbb C^5\) restricted from \(SU(5)\)]]. In the \(E_7\) construction, three subspaces carry three copies of this \(\mathfrak g_{\mathrm{SM}}\)-module. That is a mathematical multiplicity statement, not by itself a dynamical explanation of flavor.

## References

1. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §§2.3 and 3.1.
2. John C. Baez, “Three Generations in \(E_7\),” 2026. [arXiv record](https://arxiv.org/abs/2608.06271). Relevant: §§1 and 9–10.
3. David Tong, “The Standard Model,” lecture notes, 2017. [arXiv record](https://arxiv.org/abs/1606.06687).
