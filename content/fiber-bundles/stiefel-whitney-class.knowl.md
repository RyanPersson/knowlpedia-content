+++
id = "fiber-bundles/stiefel-whitney-class"
title = "Stiefel–Whitney class"
kind = "definition"
summary = "A canonical mod-2 characteristic class of a real vector bundle."
aliases = ["total Stiefel-Whitney class"]
domains = ["fiber-bundles", "topology"]
prerequisites = ["fiber-bundles/vector-bundle", "topology/singular-cohomology-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a rank-\(r\) real [[fiber-bundles/vector-bundle|vector bundle]] \(E\to X\), its **Stiefel–Whitney classes** are canonical elements [[topology/singular-cohomology-group|\(w_i(E)\in H^i(X;\mathbb Z/2)\)]], for \(0\leq i\leq r\), with \(w_0(E)=1\) and \(w_i(E)=0\) for \(i>r\). The **total Stiefel–Whitney class** is
\[
w(E)=1+w_1(E)+\cdots+w_r(E).
\]
The classes are characterized by naturality under pullback, the [[fiber-bundles/whitney-sum-formula|Whitney product formula]] \(w(E\oplus F)=w(E)\smile w(F)\), and the normalization that the first class of the tautological real line bundle over \(\mathbb{RP}^{\infty}\) generates \(H^1(\mathbb{RP}^{\infty};\mathbb Z/2)\).

## Basic properties

If \(f:Y\to X\) is continuous, then
\[
w_i(f^*E)=f^*w_i(E).
\]
The Whitney product formula implies that a [[algebra-modules/short-exact-sequence|short exact sequence]]
\[
0\longrightarrow E'\longrightarrow E\longrightarrow E''\longrightarrow0
\]
satisfies \(w(E)=w(E')\smile w(E'')\), since such a sequence of real vector bundles splits after choosing a [[fiber-bundles/bundle-metric|bundle metric]]. Trivial bundles have total class \(1\).

These axioms uniquely determine the classes and make them insensitive to choices of metrics, connections, or [[fiber-bundles/local-trivialization|local trivializations]].

## Geometric meaning

The first class \(w_1(E)\) vanishes exactly when \(E\) is orientable. For an oriented bundle, \(w_2(E)\) is the primary obstruction to a [[fiber-bundles/spin-structure|spin structure]]. More generally, nonzero higher classes obstruct the existence of many everywhere linearly independent sections: if \(E\) has \(k\) pointwise independent sections, then the top \(k\) Stiefel–Whitney classes vanish.

For a closed smooth \(n\)-manifold \(M\), evaluating degree-\(n\) products of the classes of \(TM\) on the mod-2 [[topology/fundamental-class|fundamental class]] gives Stiefel–Whitney numbers. These numbers are central invariants in unoriented cobordism.

## Examples

For the tautological real [[fiber-bundles/line-bundle|line bundle]] \(\gamma^1\to\mathbb{RP}^n\), \(w(\gamma^1)=1+a\), where \(a\) is the generator of \(H^1(\mathbb{RP}^n;\mathbb Z/2)\). For the [[fiber-bundles/tangent-bundle|tangent bundle]] of the sphere,
\[
TS^n\oplus\underline{\mathbb R}\cong\underline{\mathbb R}^{\,n+1},
\]
so the Whitney formula gives \(w(TS^n)=1\).

Because coefficients are mod \(2\), no orientation is required to define these classes. Integral lifts or refinements, when they exist, are additional structure and are not part of the definition.

## Conventions and scope

The singular title “Stiefel–Whitney class” refers to any component \(w_i(E)\); the plural refers to the whole family. These are invariants of real vector bundles. Chern classes play the analogous role for complex bundles, although reduction mod \(2\) relates the even Stiefel–Whitney classes of an underlying real bundle to Chern classes.

**Warning.** The notation \(w_i\) records cohomological degree \(i\), not half the degree. The cup product and all coefficients in this knowl are taken in \(\mathbb Z/2\).

## References

1. J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Chapters 4 and 8, axioms, examples, and obstruction-theoretic properties.
2. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 17, characteristic classes of real vector bundles.
