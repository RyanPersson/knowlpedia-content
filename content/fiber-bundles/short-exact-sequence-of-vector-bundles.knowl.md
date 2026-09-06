+++
id = "fiber-bundles/short-exact-sequence-of-vector-bundles"
title = "Short exact sequence of vector bundles"
kind = "definition"
summary = "A pair of bundle morphisms whose induced sequence is exact in every fiber."
aliases = ["exact sequence of smooth vector bundles"]
domains = ["fiber-bundles"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/vector-bundle-morphism", "fiber-bundles/kernel-and-image-bundles-of-a-constant-rank-morphism", "fiber-bundles/bundle-isomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **short exact sequence of smooth vector bundles** over a manifold \(M\) is a diagram of [[fiber-bundles/vector-bundle|vector bundles]] and [[fiber-bundles/vector-bundle-morphism|bundle morphisms]] over \(M\),
\[
0\longrightarrow E'
\overset{\iota}{\longrightarrow}E
\overset{q}{\longrightarrow}E''
\longrightarrow0,
\]
such that for every \(x\in M\) the vector-space sequence
\[
0\longrightarrow E'_x
\overset{\iota_x}{\longrightarrow}E_x
\overset{q_x}{\longrightarrow}E''_x
\longrightarrow0
\]
is exact. Equivalently, \(\iota\) identifies \(E'\) with the [[fiber-bundles/kernel-and-image-bundles-of-a-constant-rank-morphism|kernel bundle]] of \(q\), and \(q\) induces a [[fiber-bundles/bundle-isomorphism|bundle isomorphism]] \(E/\iota(E')\cong E''\).
Exactness therefore records both the embedded subbundle and its associated quotient bundle.

## Immediate consequences

Fiberwise exactness implies
\[
\operatorname{rank}E=\operatorname{rank}E'+\operatorname{rank}E''.
\]
The morphism \(\iota\) has constant rank and realizes \(E'\) as a [[fiber-bundles/vector-subbundle|vector subbundle]] of \(E\); the morphism \(q\) is fiberwise surjective. Conversely, every vector subbundle \(E'\subseteq E\) produces the canonical exact sequence
\[
0\longrightarrow E'\longrightarrow E\longrightarrow E/E'\longrightarrow0.
\]

Bundle pullback preserves [[algebra-modules/short-exact-sequence|short exact sequences]], because taking each pulled-back fiber reproduces the original exact vector-space sequence.

## Splittings

A **splitting** is a [[fiber-bundles/bundle-morphism|bundle morphism]] \(\sigma:E''\to E\) with \(q\circ\sigma=\operatorname{id}_{E''}\). Such a choice gives an isomorphism
\[
E'\oplus E''\longrightarrow E,
\qquad
(u,v)\longmapsto\iota(u)+\sigma(v).
\]
On a paracompact [[fiber-bundles/smooth-manifold|smooth manifold]], every short exact sequence of finite-rank smooth vector bundles splits: choose a [[fiber-bundles/bundle-metric|bundle metric]] on \(E\) and take the [[linear-algebra/orthogonal-complement|orthogonal complement]] of \(\iota(E')\). The splitting is generally noncanonical. This differs from exact sequences of [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundles]], which need not split holomorphically.

## Standard examples

For an [[differential-geometry/embedded-submanifold|embedded submanifold]] \(N\subseteq M\), the tangent-normal sequence
\[
0\longrightarrow TN\longrightarrow TM|_N\longrightarrow \nu N\longrightarrow0
\]
is short exact. For a constant-rank bundle morphism \(\Phi:E\to F\), its kernel and image give
\[
0\longrightarrow\ker\Phi\longrightarrow E\longrightarrow\operatorname{im}\Phi\longrightarrow0.
\]
These examples organize geometric information that would otherwise be recorded only as unrelated fiberwise statements.

## References

1. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 3, exact sequences and splitting of vector bundles.
2. L. W. Tu, *Differential Geometry: Connections, Curvature, and Characteristic Classes*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-55092-8). Relevant: Chapter 1, vector-bundle operations and exact sequences.
