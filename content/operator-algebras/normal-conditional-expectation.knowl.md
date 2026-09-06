+++
id = "operator-algebras/normal-conditional-expectation"
title = "Normal conditional expectation"
kind = "definition"
summary = "An ultraweakly continuous conditional expectation from a von Neumann algebra onto a von Neumann subalgebra."
aliases = ["von Neumann algebra conditional expectation", "normal expectation"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/conditional-expectation", "operator-algebras/normal-positive-map"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(N\subseteq M\) be unital
[[operator-algebras/von-neumann-algebra|von Neumann algebras]] with the same
identity. A **normal conditional expectation** \(E:M\to N\) is a
[[operator-algebras/conditional-expectation|conditional expectation]] that
is [[operator-algebras/normal-positive-map|normal]]. Explicitly, \(E\) is a
positive norm-one linear projection onto \(N\) and, for every bounded
increasing net \((x_i)\) in \(M_+\),
\[
E\!\left(\sup_i x_i\right)=\sup_i E(x_i).
\]
The norm-one projection property implies
\(E(n_1xn_2)=n_1E(x)n_2\) for \(n_1,n_2\in N\). Normality is the additional
compatibility with ultraweak limits; faithfulness is not included.

## Equivalent formulations

Because \(E\) is bounded, normality is equivalent to the existence of a
preadjoint
\[
E_*:N_*\longrightarrow M_*,
\qquad E_*(\omega)=\omega\circ E.
\]
It is also equivalent to preservation of suprema of bounded increasing nets
of projections. Tomiyama's theorem supplies positivity, complete positivity,
and \(N\)-bimodularity from the norm-one projection hypothesis.

## Examples and a near-miss

On \(B(\ell^2)\), taking the diagonal matrix entries defines a normal faithful
conditional expectation onto the diagonal von Neumann algebra
\(\ell^\infty\). More generally, averaging a normal action of a compact group
against [[harmonic-analysis/haar-measure|Haar measure]] gives a normal
conditional expectation onto the fixed-point algebra.

If \(\varphi\) is a singular state on \(M\), then
\[
E_\varphi(x)=\varphi(x)1
\]
is a \(C^*\)-algebraic conditional expectation from \(M\) onto
\(\mathbb C1\), but it is not normal. Thus normality does not follow merely
because the domain and range are von Neumann algebras.

## Structure and consequences

The range of a normal expectation is automatically ultraweakly closed, and
normal [[operator-algebras/positive-linear-functional|positive functionals]] on \(N\) pull back to normal positive functionals
on \(M\). If \(E\) is faithful, then \(E(x^*x)=0\) implies \(x=0\); this
extra condition is often required in modular theory.

Existence is not automatic for an arbitrary inclusion \(N\subseteq M\). Given
a [[operator-algebras/faithful-normal-state|faithful normal state]]
\(\varphi\) on \(M\), Takesaki's expectation theorem characterizes the
existence of a \(\varphi\)-preserving normal conditional expectation onto
\(N\) by invariance of \(N\) under the
[[operator-algebras/modular-automorphism-group|modular automorphism group]]
\(\sigma^\varphi\).

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, §2 on norm-one projections and conditional expectations.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter IX, §4 on modular invariance and normal conditional expectations.
