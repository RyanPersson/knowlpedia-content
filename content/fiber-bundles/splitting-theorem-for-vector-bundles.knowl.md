+++
id = "fiber-bundles/splitting-theorem-for-vector-bundles"
title = "Splitting theorem for vector bundles"
kind = "theorem"
summary = "Every short exact sequence of finite-rank vector bundles over a paracompact base admits a generally noncanonical bundle splitting."
aliases = ["splitting of a vector bundle exact sequence", "bundle complement theorem"]
domains = ["fiber-bundles"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/short-exact-sequence-of-vector-bundles", "fiber-bundles/topological-real-vector-bundle", "fiber-bundles/topological-complex-vector-bundle", "fiber-bundles/paracompact-topological-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be paracompact Hausdorff, and let
\[
0\longrightarrow E'\overset{\iota}{\longrightarrow}E
\overset{q}{\longrightarrow}E''\longrightarrow0
\]
be a [[fiber-bundles/short-exact-sequence-of-vector-bundles|short exact sequence]] of finite-rank real or complex topological vector bundles over \(X\). The **splitting theorem for vector bundles** states that there is a continuous fiberwise linear bundle map \(s:E''\to E\) satisfying \(q\circ s=\operatorname{id}_{E''}\). Equivalently,
\[
E\cong E'\oplus E''
\]
through an isomorphism that identifies \(\iota\) with inclusion of the first summand and \(q\) with projection onto the second. Here the direct sum uses fiberwise direct sums with their bundle topology. For a smooth exact sequence over a smooth manifold, the splitting and isomorphism may be chosen smooth. A splitting exists, but the theorem does not select a canonical one.

## Proof idea

Paracompactness provides a continuous positive-definite fiber metric on \(E\) (a Hermitian metric in the complex case), which may be chosen smooth for smooth bundles. The image \(\iota(E')\) is a subbundle, and its fiberwise [[linear-algebra/orthogonal-complement|orthogonal complement]] \(\iota(E')^\perp\) is another subbundle. The restriction
\[
q|_{\iota(E')^\perp}:\iota(E')^\perp\longrightarrow E''
\]
is a fiberwise isomorphism and hence a bundle isomorphism in the chosen topological or smooth category. Its inverse, followed by the inclusion into \(E\), is the required right inverse \(s\).

Different bundle metrics generally produce different complements. The resulting direct-sum decompositions are therefore auxiliary choices rather than additional structure carried by the original exact sequence.

## Consequences and limits

Every vector subbundle \(F\subseteq E\) over a paracompact base has a complementary subbundle \(F^\perp\) with \(E\cong F\oplus F^\perp\). On sections, a chosen splitting decomposes each section of \(E\) into components in the two summands.

**Warning.** This is a theorem in the topological or smooth vector-bundle category. A [[algebra-modules/short-exact-sequence|short exact sequence]] of [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundles]] need not split holomorphically, because a smooth orthogonal complement need not be a holomorphic subbundle. Paracompactness is also doing real work: it is what guarantees the global metric used in the proof.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: chapter 3, bundle metrics, complements, and exact sequences of vector bundles.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: chapter 10, vector bundles, bundle metrics, and orthogonal complements.
