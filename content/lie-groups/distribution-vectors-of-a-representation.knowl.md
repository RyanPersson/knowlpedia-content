+++
id = "lie-groups/distribution-vectors-of-a-representation"
title = "Distribution vectors of a Lie-group representation"
kind = "definition"
summary = "Continuous antilinear functionals on the Fréchet space of smooth vectors of a Lie-group representation."
aliases = ["generalized vectors", "distribution globalization", "H-infinity dual"]
domains = ["lie-groups", "functional-analysis"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/smooth-vector-unitary-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and let \((\pi,\mathcal H)\) be a strongly continuous
unitary representation. Write \(\mathcal H^\infty\) for its
[[lie-groups/smooth-vector-unitary-representation|space of smooth vectors]],
with the usual Fréchet topology. The space of **distribution vectors** is
\[
\mathcal H^{-\infty}=(\mathcal H^\infty)'_{\mathrm{anti}},
\]
the continuous antilinear dual of \(\mathcal H^\infty\), equipped usually
with its strong dual topology. The Hilbert-space pairing gives continuous
dense inclusions
\[
\mathcal H^\infty\subseteq\mathcal H\subseteq\mathcal H^{-\infty}.
\]
Thus a distribution vector is a generalized vector acting continuously on
smooth test vectors, not necessarily an element of \(\mathcal H\).

## The smooth-vector topology

Choose a finite basis of the complexified [[lie-groups/lie-algebra|Lie algebra]] and take all ordered
monomials in that basis. Equivalently, let \(D\) range over a vector-space
basis of the universal [[lie-groups/universal-enveloping-algebra|enveloping algebra]]. Seminorms of the form
\[
v\longmapsto\lVert d\pi(D)v\rVert,\qquad D\in U(\mathfrak g_{\mathbb C}),
\]
define the Fréchet topology on \(\mathcal H^\infty\). Different finite bases
or [[algebra-groups/generating-set|generating sets]] of \(\mathfrak g_{\mathbb C}\), together with all
monomials in them, give equivalent countable seminorm families. No single
finite collection of these seminorms generally suffices. Continuity with
respect to the full family distinguishes distribution vectors from arbitrary
algebraic functionals.

## Extended group and Lie-algebra actions

The contragredient action is defined by
\[
(\pi^{-\infty}(g)\lambda)(v)=\lambda(\pi(g^{-1})v).
\]
Differentiating on the test-vector side extends the
[[lie-groups/derived-representation-on-smooth-vectors|derived
representation]] to distribution vectors:
\[
(d\pi^{-\infty}(X)\lambda)(v)=-\lambda(d\pi(X)v).
\]
These formulas are well-defined because the original action preserves
\(\mathcal H^\infty\) continuously.

## Use in representation theory

Distribution vectors allow [[fiber-bundles/equivariant-map|equivariant maps]] to be encoded by generalized
matrix coefficients and invariant functionals. Delta distributions in
geometric realizations and automorphic distribution vectors are typical
examples. In the representation theory of real reductive groups, the passage
between smooth globalizations and their distribution duals is a basic tool;
it is broader than the Hilbert-space representation and must retain the
chosen locally convex topology.

## References

1. Nolan R. Wallach, *Real Reductive Groups I*, Pure and Applied Mathematics 132, Academic Press, 1988. [WorldCat record](https://search.worldcat.org/title/15055114). Relevant: §4.4 on smooth and distribution vectors.
2. W. Casselman, “Canonical Extensions of Harish-Chandra Modules to Representations of \(G\),” *Canadian Journal of Mathematics* 41 (1989), 385–438. [DOI record](https://doi.org/10.4153/CJM-1989-019-5). Relevant: smooth globalizations and distributional duality.
