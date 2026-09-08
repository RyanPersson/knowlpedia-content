+++
id = "fiber-bundles/stiefel-whitney-class"
title = "Stiefel–Whitney class"
kind = "definition"
summary = "A canonical mod-2 characteristic class of a real vector bundle."
aliases = ["total Stiefel-Whitney class"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/topological-real-vector-bundle", "topology/singular-cohomology-group", "topology/cup-product-and-cohomology-ring", "fiber-bundles/paracompact-topological-space", "differential-geometry/real-projective-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For a rank-\(r\) [[fiber-bundles/topological-real-vector-bundle|topological real vector bundle]] \(E\to X\) over a paracompact Hausdorff space, its **Stiefel–Whitney classes** are classes
\[
w_i(E)\in H^i(X;\mathbb Z/2),\qquad i\ge0,
\]
depending only on the bundle isomorphism class. As a family over all such bundles and bases they are characterized by all of the following axioms:

1. **Degree and rank normalization:** \(w_0(E)=1\) and \(w_i(E)=0\) for \(i>r\).
2. **Naturality:** for every continuous \(f:Y\to X\) with \(Y\) paracompact Hausdorff, \(w_i(f^*E)=f^*w_i(E)\).
3. **Whitney product:** \(w(E\oplus F)=w(E)\smile w(F)\), where \(w(E)=\sum_{i=0}^r w_i(E)\), direct sums are fiberwise direct sums with their local product topology, and multiplication is the mod-\(2\) [[topology/cup-product-and-cohomology-ring|cup product]].
4. **Line normalization:** the tautological real line bundle \(\gamma^1\) over \(\mathbb{RP}^1\) has \(w_1(\gamma^1)\) equal to the nonzero element of \(H^1(\mathbb{RP}^1;\mathbb Z/2)\). Its fiber over a line \(\ell\subset\mathbb R^2\) is \(\ell\) itself.

The class \(w(E)\) is the **total Stiefel–Whitney class**. These axioms include the normalization that distinguishes this canonical family from other natural mod-\(2\) classes.

## Basic properties

If \(f:Y\to X\) is continuous, then
\[
w_i(f^*E)=f^*w_i(E).
\]
The Whitney product formula implies that a fiberwise exact sequence of real vector bundles
\[
0\longrightarrow E'\longrightarrow E\longrightarrow E''\longrightarrow0
\]
satisfies \(w(E)=w(E')\smile w(E'')\), since such a sequence of real vector bundles splits after choosing a continuous fiber metric. Trivial bundles have total class \(1\).

These axioms uniquely determine the classes and make them insensitive to choices of metrics, connections, or [[fiber-bundles/local-trivialization|local trivializations]].

## Geometric meaning

The first class \(w_1(E)\) vanishes exactly when \(E\) is orientable. For an oriented positive-rank bundle, \(w_2(E)\) obstructs a lift of its oriented orthonormal frame bundle through \(\operatorname{Spin}(r)\to\operatorname{SO}(r)\); for tangent bundles this is a [[fiber-bundles/spin-structure|spin structure]]. More generally, nonzero higher classes obstruct the existence of many everywhere linearly independent sections: if \(E\) has \(k\) pointwise independent sections, then the top \(k\) Stiefel–Whitney classes vanish.

For a closed smooth \(n\)-manifold \(M\), evaluating degree-\(n\) products of the classes of \(TM\) on the mod-2 [[topology/fundamental-class|fundamental class]] gives Stiefel–Whitney numbers. These numbers are central invariants in unoriented cobordism.

## Examples

For \(n\ge1\), the tautological real line bundle \(\gamma^1\to\mathbb{RP}^n\), \(w(\gamma^1)=1+a\), where \(a\) is the generator of \(H^1(\mathbb{RP}^n;\mathbb Z/2)\). For the [[fiber-bundles/tangent-bundle|tangent bundle]] of the sphere,
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
