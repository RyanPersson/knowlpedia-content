+++
id = "langlands/iwahori-level-structure"
title = "Iwahori level structure"
kind = "definition"
summary = "A level structure defined by the inverse image of a Borel subgroup under evaluation of positive loops at the marked point."
aliases = ["Borel level structure"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/borel-subgroup", "langlands/level-structure-on-g-bundle", "langlands/parahoric-level-structure"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over \(k\), choose a
[[algebraic-geometry-foundations/borel-subgroup|Borel subgroup]]
\(B\subseteq G\), and let
\[
I=\{g\in G(k\lbrack\!\lbrack t\rbrack\!\rbrack):g(0)\in B\}.
\]
An **Iwahori level structure** on a \(G\)-bundle at a marked point is a
[[langlands/level-structure-on-g-bundle|reduction of its formal-frame torsor]]
to \(I\).

The Iwahori subgroup is a
[[langlands/parahoric-level-structure|parahoric]] subgroup; equivalently, an
Iwahori level structure is a reduction of the fiber at the marked point to
\(B\).

## References

1. Georgios Pappas and Michael Rapoport, “Twisted loop groups and their
   affine flag varieties,” *Advances in Mathematics* 219 (2008), 118–198.
   [arXiv](https://arxiv.org/abs/math/0607130).
