+++
id = "algebraic-geometry-foundations/flag-variety"
title = "Flag variety"
kind = "definition"
summary = "A projective homogeneous variety parametrizing flags, realized for a reductive group as a quotient by a parabolic subgroup."
aliases = ["flag variety", "generalized flag variety"]
domains = ["algebraic-geometry-foundations", "langlands"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/parabolic-subgroup", "algebraic-geometry-foundations/borel-subgroup"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
algebraic group]] over a field \(k\), and let \(P\subseteq G\) be a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]]. The
quotient \(G/P\) is a **flag variety**. When
\(P=B\) is a [[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]],
\(G/B\) is the complete flag variety.

For \(G=GL_n\), these varieties parametrize chains
\[
0\subset V_{d_1}\subset\cdots\subset V_{d_r}\subset k^n,
\qquad \dim V_{d_i}=d_i.
\]
The complete flag variety uses every dimension \(1,\ldots,n-1\).

## Geometry

Flag varieties are smooth and projective. The group \(G\) acts transitively,
and the stabilizer of the base flag is \(P\). Their Bruhat decompositions are
indexed by suitable cosets in the [[lie-groups/weyl-group|Weyl group]].

The rank-one case
[[algebraic-geometry-foundations/projective-line-as-rank-one-flag-variety|\(SL_2/B\simeq\mathbb P^1\)]]
is the simplest example.

## References

1. Claude Chevalley, “Sur les décompositions cellulaires des espaces
   \(G/B\),” in *Algebraic Groups and Their Generalizations: Classical
   Methods*, Proc. Sympos. Pure Math. 56 (1994), 1–23
   (manuscript originally circulated in 1958).
