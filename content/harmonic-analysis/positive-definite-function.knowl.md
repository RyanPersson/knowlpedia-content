+++
id = "harmonic-analysis/positive-definite-function"
title = "Positive-definite function on a group"
kind = "definition"
summary = "A positive-definite function is a continuous scalar function whose group-difference matrices are positive semidefinite."
aliases = ["function of positive type", "positive type function"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]]. A continuous
function \(\varphi:G\to\mathbb C\) is **positive-definite** if, for every
finite choice \(g_1,\ldots,g_n\in G\) and \(c_1,\ldots,c_n\in\mathbb C\),
\[
\sum_{i,j=1}^n c_i\overline{c_j}\,
\varphi(g_j^{-1}g_i)\geq 0.
\]
Equivalently, the matrix
\(\bigl[\varphi(g_j^{-1}g_i)\bigr]_{i,j}\) is
[[linear-algebra/positive-semidefinite-matrix|positive semidefinite]] for every
finite tuple. The inequality is real despite being written with complex
entries. Continuity is part of the topological-group definition used here; on
an abstract group, the same positivity condition can be imposed without it.

## Representation-theoretic characterization

Every function of the form
\(\varphi(g)=\langle\pi(g)\xi,\xi\rangle\), where \(\pi\) is a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]],
is positive-definite. Conversely, the
[[harmonic-analysis/gns-construction-positive-definite-function|Gelfand–Naimark–Segal construction]]
realizes every continuous
positive-definite function in this way with a
[[lie-groups/cyclic-vector-and-cyclic-representation|cyclic vector]], uniquely up to
[[lie-groups/unitary-equivalence-of-representations|unitary equivalence]] when
the cyclic realization is minimal
[Folland, §3.3].

## Basic properties

Positivity gives
\(\varphi(e)\geq0\),
\(\varphi(g^{-1})=\overline{\varphi(g)}\), and
\(\lvert\varphi(g)\rvert\leq\varphi(e)\). If \(\varphi(e)=1\), the associated
[[operator-algebras/cyclic-vector|cyclic vector]] can be chosen to have norm one. Products and nonnegative linear
combinations of positive-definite functions are again positive-definite.

## Conventions and scope

The displayed formula uses an [[linear-algebra/inner-product|inner product]]
linear in its first variable. Positive-definiteness does not imply conjugation
invariance, so a positive-definite function need not be an
[[algebra-groups/class-function|class function]]. For
[[algebra-groups/abelian-group|abelian groups]], normalized continuous examples
include [[probability/characteristic-function-probability|characteristic functions]]
arising as Fourier transforms of
[[probability/probability-measure|probability measures]].

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.3 on positive-definite functions and cyclic representations.
2. Bachir Bekka, Pierre de la Harpe, and Alain Valette, *Kazhdan's Property (T)*, Cambridge University Press, 2008. [DOI record](https://doi.org/10.1017/CBO9780511542749). Relevant: Appendix C on positive-definite functions.
