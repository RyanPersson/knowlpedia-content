+++
id = "harmonic-analysis/weak-containment-unitary-representations"
title = "Weak containment of unitary representations"
kind = "definition"
summary = "One unitary representation is weakly contained in another when its diagonal coefficients are locally approximable by finite sums from the other."
aliases = ["weak containment", "Fell weak containment", "representation weakly contained"]
domains = ["harmonic-analysis", "lie-groups", "operator-algebras"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]], and
let \(\pi\) and \(\rho\) be
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representations]]
on [[linear-algebra/hilbert-space|Hilbert spaces]]
\(H_\pi\) and \(H_\rho\).
The representation \(\pi\) is **weakly contained** in \(\rho\), written
\(\pi\prec\rho\), if for every \(\xi\in H_\pi\),
[[topology/compact-set|compact set]] \(K\subseteq G\),
and \(\varepsilon>0\), there exist
\(\eta_1,\ldots,\eta_n\in H_\rho\) such that
\[
\left|\langle\pi(g)\xi,\xi\rangle-
\sum_{k=1}^n\langle\rho(g)\eta_k,\eta_k\rangle\right|<\varepsilon
\]
for every \(g\in K\).
The integer \(n\) and the approximating vectors may depend on
\(\xi\), \(K\), and \(\varepsilon\). Thus the condition compares positive
definite diagonal coefficients uniformly on compact subsets, allowing finite
sums of coefficients of \(\rho\); it does not require an isometric embedding
of \(H_\pi\) into \(H_\rho\).

## Equivalent operator-norm criterion

For the [[harmonic-analysis/integrated-form-unitary-representation|integrated representations]] of \(L^1(G)\), weak containment is
equivalent to
\[
\lVert\pi(f)\rVert\leq\lVert\rho(f)\rVert
\qquad\text{for every }f\in L^1(G).
\]
Equivalently, after passing to the
[[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]],
\(\ker\rho\subseteq\ker\pi\). The direction of this inclusion is important:
the containing representation detects at least as large a norm. These
equivalences are part of Fell's theory of weak containment
[Fell, 1962].

## Coefficients and direct sums

The approximation condition uses diagonal
[[harmonic-analysis/coefficient-function|coefficient functions]]; polarization
recovers approximation statements for general coefficients. A finite sum of
diagonal coefficients of \(\rho\) is a single diagonal coefficient of a
finite direct sum of copies of \(\rho\). Consequently,
\(\pi\prec\rho\) and \(\rho\prec\sigma\) imply \(\pi\prec\sigma\).

## Conventions and scope

**Warning.** Weak containment is not literal containment by an invariant
subspace, and it is weaker than
[[lie-groups/unitary-equivalence-of-representations|unitary equivalence]].
Equivalent coefficient definitions may use neighborhoods in the compact-open
topology or coefficients from finite multiples of \(\rho\); the formulation
above fixes those choices explicitly.

## References

1. J. M. G. Fell, "Weak Containment and Induced Representations of Groups," *Canadian Journal of Mathematics* 14 (1962), 237–268. [DOI record](https://doi.org/10.4153/CJM-1962-016-6). Relevant: the definition and basic permanence properties of weak containment.
2. Bachir Bekka, Pierre de la Harpe, and Alain Valette, *Kazhdan's Property (T)*, Cambridge University Press, 2008. [DOI record](https://doi.org/10.1017/CBO9780511542749). Relevant: Appendix F on weak containment.
