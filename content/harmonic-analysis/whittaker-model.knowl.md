+++
id = "harmonic-analysis/whittaker-model"
title = "Whittaker model"
kind = "definition"
summary = "A realization of a generic representation using functions transforming by a nondegenerate character of a maximal unipotent subgroup."
aliases = ["Whittaker functional", "generic representation", "Whittaker realization"]
domains = ["harmonic-analysis", "langlands", "lie-groups"]
prerequisites = ["algebraic-geometry-foundations/quasi-split-reductive-group", "algebra-fields-galois/local-field", "algebraic-geometry-foundations/borel-subgroup", "harmonic-analysis/unitary-character", "algebraic-geometry-foundations/unipotent-radical", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split
reductive group]] over a
[[algebra-fields-galois/local-field|local field]], let
\(B=TU\) be
an \(F\)-rational [[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]], and let
\(\psi:U(F)\to\mathbb C^\times\) be a nondegenerate
[[harmonic-analysis/unitary-character|unitary character]] of its
[[algebraic-geometry-foundations/unipotent-radical|unipotent radical]]. A
**Whittaker functional** on a representation \((\pi,V)\) of \(G(F)\) is a
[[linear-algebra/linear-map|linear map]] \(\lambda:V\to\mathbb C\) satisfying

\[
\lambda(\pi(u)v)=\psi(u)\lambda(v)
\qquad(u\in U(F)).
\]

If a nonzero such functional exists, \(\pi\) is **\(\psi\)-generic**. The
associated **Whittaker model** is the realization by functions

\[
W_v(g)=\lambda(\pi(g)v),
\qquad
W_v(ug)=\psi(u)W_v(g).
\]

## Nondegeneracy

Nondegeneracy means that \(\psi\) is nontrivial on every simple-root quotient
of \(U\) determined by \(B\). The \(G(F)\)-conjugacy class of the pair
\((B,\psi)\) is a [[langlands/whittaker-datum|Whittaker datum]].

## Uniqueness

For irreducible admissible representations in the standard quasi-split local
setting, the Whittaker functional is unique up to scalar when it exists. This
multiplicity-one result makes the Whittaker model a canonical realization
after normalizations are chosen.

## Role in local Langlands

A Whittaker datum normalizes the internal parametrization of an
[[langlands/l-packet|\(L\)-packet]]. For a
[[harmonic-analysis/tempered-representation-p-adic-group|tempered]] packet of
a quasi-split \(p\)-adic group, the generic-packet conjecture
predicts a unique member generic for the chosen datum.

## References

1. François Rodier, “Whittaker models for admissible representations of
   reductive \(p\)-adic split groups,” in *Harmonic Analysis on Homogeneous
   Spaces*, Proceedings of Symposia in Pure Mathematics 26, 1973.
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §§2.2–2.3, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
