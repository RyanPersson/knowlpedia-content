+++
id = "langlands-letter/knowls/pinned-automorphisms"
title = "Pinning and pinned automorphisms"
kind = "knowl"
summary = "A Borel, maximal torus, and simple-root vectors that canonically lift automorphisms of a based root datum."
aliases = ["pinned-automorphisms", "Pinning and Pinned Automorphisms"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/pinned-automorphisms.md"
section_mode = "progressive"
+++

A **pinning** of a split connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] \(G\) is data

\[
(B,T,\{X_\alpha\}_{\alpha\in\Delta}),
\]

where \(B\) is a [[algebraic-geometry-foundations/borel-subgroup|Borel
subgroup]], \(T\subset B\) a
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]], and
\(X_\alpha\) a nonzero vector, or equivalently a root-group
parametrization, for every [[lie-groups/simple-root|simple root]].

A **pinned automorphism** preserves \(B\) and \(T\) and carries the chosen
simple-root parametrizations according to its induced permutation of the
[[langlands-letter/knowls/roots-weights-weyl|based root datum]]. If the
simple roots are regarded as individually labeled
and each \(X_\alpha\) is required to be fixed pointwise, the resulting
automorphism is usually the identity; diagram automorphisms require the
permutation-compatible formulation.

## Splitting outer automorphisms

For a pinned reductive group there is a canonical splitting

\[
\operatorname{Out}(G)
\simeq
\operatorname{Aut}(\Psi_0(G))
\longrightarrow
\operatorname{Aut}(G)
\]

of the passage from automorphisms to the based root datum. This realizes
Dynkin-diagram automorphisms as actual group automorphisms without an
inner-automorphism ambiguity.

## L-group role

For a reductive group over a nonsplit field, the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
acts on its based root
datum. A pinning of the
[[langlands-letter/knowls/langlands-dual-group|dual group]] \(\widehat G\)
lifts this action to automorphisms and defines the
[[algebra-groups/semidirect-product|semidirect-product]] presentation of the
[[langlands/l-group|\(L\)-group]]. Changing the pinning changes the
presentation by an inner isomorphism.

## Relation to the letter

The letter's group \(\Omega\) acts on pinned root data and hence on the dual
construction. Modern terminology makes explicit whether an automorphism
fixes labels pointwise or permutes them through a diagram automorphism.

## References

1. T. A. Springer, *Linear Algebraic Groups*, second edition, Birkhäuser,
   1998.
2. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” §2.1.
   [arXiv](https://arxiv.org/abs/1009.0785).
