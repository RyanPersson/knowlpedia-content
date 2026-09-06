+++
id = "langlands-letter/knowls/coroots-and-pairing"
title = "Coroots and the character-cocharacter pairing"
kind = "knowl"
summary = "Coroots and their integral pairing with characters, controlling dominance and dual root data."
aliases = ["coroots-and-pairing", "Coroots and the Weight–Coroot Pairing"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/coroots-and-pairing.md"
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/maximal-torus-weight-lattice", "langlands-letter/knowls/roots-weights-weyl"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]]
\(T\), its characters and cocharacters have the perfect
pairing

\[
\langle\ ,\ \rangle:
X^*(T)\times X_*(T)\longrightarrow\mathbb Z
\]

defined by

\[
\lambda\circ\mu(z)=z^{\langle\lambda,\mu\rangle}.
\]

For every [[langlands-letter/knowls/roots-weights-weyl|root]]
\(\alpha\in\Phi\subset X^*(T)\), the root datum specifies a
**coroot** \(\alpha^\vee\in X_*(T)\) satisfying

\[
\langle\alpha,\alpha^\vee\rangle=2.
\]

## Reflections and dominance

The root and coroot define reflections

\[
s_\alpha(\lambda)
=
\lambda-\langle\lambda,\alpha^\vee\rangle\alpha,
\qquad
s_\alpha(\mu)
=
\mu-\langle\alpha,\mu\rangle\alpha^\vee.
\]

A character \(\lambda\) is dominant relative to a
[[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]] if
\(\langle\lambda,\alpha^\vee\rangle\geq0\) for every [[lie-groups/simple-root|simple root]]
\(\alpha\).

## Lie-algebra interpretation

Differentiating \(\alpha^\vee\) gives a Cartan element \(H_\alpha\). With
the standard normalization,

\[
d\lambda(H_\alpha)
=
\langle\lambda,\alpha^\vee\rangle.
\]

In positive characteristic,
[[algebraic-geometry-foundations/group-scheme|group-scheme]]
[[langlands-letter/knowls/roots-weights-weyl|root data]] remain the safer
definition because differential maps can lose information.

## Langlands duality

The dual based root datum exchanges

\[
(X^*(T),\Phi)
\quad\text{with}\quad
(X_*(T),\Phi^\vee).
\]

This exchange defines the
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]] and
turns [[langlands/dominant-coweight|dominant coweights]] of \(G\) into dominant weights of \(\widehat G\).

## References

1. A. Borel, *Linear Algebraic Groups*, second edition, Springer, 1991.
