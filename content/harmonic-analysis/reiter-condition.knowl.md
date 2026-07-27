+++
id = "harmonic-analysis/reiter-condition"
title = "Reiter condition"
kind = "definition"
summary = "An analytic approximation condition asserting the existence of normalized nonnegative L1 functions that are uniformly almost invariant on compact sets."
aliases = ["Reiter property P1", "Reiter net", "almost invariant L1 functions"]
domains = ["harmonic-analysis", "functional-analysis", "topology"]
section_mode = "progressive"
+++

A [[topology/locally-compact-group|locally compact group]] \(G\) satisfies
the **Reiter condition \(P_1\)** if there is a net
\((u_i)\) in the [[harmonic-analysis/l1-group-algebra|\(L^1\) group algebra]] such that \(u_i\geq0\), \(\lVert u_i\rVert_1=1\), and, for every
compact subset \(C\subseteq G\),
\[
\sup_{x\in C}\lVert L_xu_i-u_i\rVert_1\longrightarrow0,
\qquad
(L_xu)(y)=u(x^{-1}y).
\]
The \(L^1\) space is formed using a left
[[harmonic-analysis/haar-measure|Haar measure]]. The condition is independent
of its normalization and requires uniform almost invariance on each compact
set, not merely [[real-analysis/pointwise-convergence|pointwise convergence]] for each fixed group element. Such a
net is called a **Reiter net**.

## Equivalence with amenability

Reiter's theorem states that \(G\) satisfies \(P_1\) exactly when \(G\) is
[[harmonic-analysis/amenable-locally-compact-group|amenable]]
[Reiter–Stegeman, Chapter 8](https://doi.org/10.1093/oso/9780198511892.001.0001).
Weak-star cluster points of the associated averaging functionals produce an
[[harmonic-analysis/invariant-mean|invariant mean]]. Conversely, an invariant
mean yields almost invariant
normalized functions through a convexity and approximation argument.

## Standard models

If \(G\) is compact, the constant density obtained from normalized Haar
measure is exactly invariant, so a constant net verifies \(P_1\). For a
discrete group, [[topology/compact-set|compact sets]] are finite and the condition becomes the
existence of probability masses in \(\ell^1(G)\) that are asymptotically
invariant under translation on every finite set. Normalized indicators of a
[[harmonic-analysis/folner-condition|Følner net]] give the basic example
[Paterson, Chapter 4](https://doi.org/10.1090/surv/029).

## Variants and conventions

Equivalent formulations allow signed functions of norm one after taking
[[real-analysis/absolute-value|absolute values]], or require convergence separately for each \(x\) together
with standard uniformization on compact sets. Conditions \(P_p\) for
\(1\leq p<\infty\) use almost invariant unit vectors in \(L^p(G)\); they are
also equivalent to amenability under the usual locally compact hypotheses
[Reiter–Stegeman, Chapter 8](https://doi.org/10.1093/oso/9780198511892.001.0001).

## References

1. Hans Reiter and Jan D. Stegeman, *Classical Harmonic Analysis and Locally Compact Groups*, 2nd ed., London Mathematical Society Monographs 22, Oxford University Press, 2000. [OUP DOI record](https://doi.org/10.1093/oso/9780198511892.001.0001). Relevant: Chapter 8 on Reiter conditions and amenability.
2. Alan L. T. Paterson, *Amenability*, Mathematical Surveys and Monographs 29, American Mathematical Society, 1988. [AMS DOI record](https://doi.org/10.1090/surv/029). Relevant: Chapter 4 on analytic characterizations of amenability.
