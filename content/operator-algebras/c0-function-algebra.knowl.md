+++
id = "operator-algebras/c0-function-algebra"
title = "C*-algebra C_0(X)"
kind = "definition"
summary = "The C*-algebra of continuous complex-valued functions that vanish at infinity on a locally compact space."
aliases = ["continuous functions vanishing at infinity", "C0(X)"]
domains = ["operator-algebras", "topology"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-space", "topology/compact-set", "operator-algebras/commutative-cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[topology/locally-compact-space|locally compact Hausdorff
space]]. The **\(C^*\)-algebra \(C_0(X)\)** consists of the continuous
functions \(f:X\to\mathbb C\) that **vanish at infinity**: for every
\(\varepsilon>0\), there is a [[topology/compact-set|compact set]]
\(K\subseteq X\) such that
\(|f(x)|<\varepsilon\) whenever \(x\notin K\). Addition, multiplication, and
involution are pointwise, with \(f^*(x)=\overline{f(x)}\), and the norm is
\(\|f\|_\infty=\sup_{x\in X}|f(x)|\). With these operations \(C_0(X)\) is a
[[operator-algebras/commutative-cstar-algebra|commutative \(C^*\)-algebra]].
It is unital exactly when \(X\) is compact.

## Relation to compact support

Every compactly supported continuous function belongs to \(C_0(X)\), and the
subalgebra \(C_c(X)\) of such functions is dense in \(C_0(X)\) for the
uniform norm. Vanishing at infinity does not require compact support: on
\(\mathbb R\), the function \(x\mapsto(1+x^2)^{-1}\) lies in \(C_0(\mathbb
R)\) but has noncompact support.

## Spectrum and unitization

The characters of \(C_0(X)\) are precisely the evaluation maps
\(f\mapsto f(x)\) for \(x\in X\). Thus locally compact [[operator-algebras/gelfand-duality|Gelfand duality]]
recovers \(X\) as the character space of \(C_0(X)\). When \(X\) is
noncompact, the [[operator-algebras/unitization|minimal unitization]] of
\(C_0(X)\) is naturally isomorphic to the continuous functions on the
one-point compactification of \(X\).

## Why it is canonical

The passage \(X\mapsto C_0(X)\) converts proper [[topology/continuous-map|continuous maps]] contravariantly
into nondegenerate \(*\)-homomorphisms. It is the locally compact,
generally nonunital counterpart of the compact-space algebra \(C(X)\), and
is the basic commutative model for ideals, spectra, and
[[operator-algebras/multiplier-algebra|multiplier algebras]].

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [Publisher record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Chapter 2 on commutative \(C^*\)-algebras and their spectra.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, second edition edited by Søren Eilers and Dorte Olesen, Academic Press, 2018. [Publisher record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the opening chapters on locally compact function algebras.
