+++
id = "fiber-bundles/splitting-theorem-for-vector-bundles"
title = "Splitting theorem for vector bundles"
kind = "theorem"
summary = "Every short exact sequence of finite-rank vector bundles over a paracompact base admits a generally noncanonical bundle splitting."
aliases = ["splitting of a vector bundle exact sequence", "bundle complement theorem"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(X\) be paracompact, and let
\[
0\longrightarrow E'\overset{\iota}{\longrightarrow}E
\overset{q}{\longrightarrow}E''\longrightarrow0
\]
be a [[fiber-bundles/short-exact-sequence-of-vector-bundles|short exact sequence]] of finite-rank real or complex [[fiber-bundles/vector-bundle|vector bundles]] over \(X\). The **splitting theorem for vector bundles** states that there is a [[fiber-bundles/vector-bundle-morphism|bundle morphism]] \(s:E''\to E\) satisfying \(q\circ s=\operatorname{id}_{E''}\). Equivalently,
\[
E\cong E'\oplus E''
\]
through an isomorphism that identifies \(\iota\) with inclusion of the first summand and \(q\) with projection onto the second. A splitting exists, but the theorem does not select a canonical one.

## Proof idea

Paracompactness provides a [[fiber-bundles/bundle-metric|bundle metric]] on \(E\). The image \(\iota(E')\) is a subbundle, and its fiberwise [[linear-algebra/orthogonal-complement|orthogonal complement]] \(\iota(E')^\perp\) is another subbundle. The restriction
\[
q|_{\iota(E')^\perp}:\iota(E')^\perp\longrightarrow E''
\]
is a fiberwise isomorphism and hence a [[fiber-bundles/bundle-isomorphism|bundle isomorphism]]. Its inverse, followed by the inclusion into \(E\), is the required right inverse \(s\) [Husemoller, chapter 3](https://doi.org/10.1007/978-1-4757-2261-1).

Different bundle metrics generally produce different complements. The resulting direct-sum decompositions are therefore auxiliary choices rather than additional structure carried by the original exact sequence.

## Consequences and limits

Every [[fiber-bundles/vector-subbundle|vector subbundle]] \(F\subseteq E\) over a paracompact base has a complementary subbundle \(F^\perp\) with \(E\cong F\oplus F^\perp\). On sections, a chosen splitting decomposes each section of \(E\) into components in the two summands.

**Warning.** This is a theorem in the topological or smooth vector-bundle category. A [[algebra-modules/short-exact-sequence|short exact sequence]] of [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundles]] need not split holomorphically, because a smooth orthogonal complement need not be a holomorphic subbundle. Paracompactness is also doing real work: it is what guarantees the global metric used in the proof.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: chapter 3, bundle metrics, complements, and exact sequences of vector bundles.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: chapter 10, vector bundles, bundle metrics, and orthogonal complements.
