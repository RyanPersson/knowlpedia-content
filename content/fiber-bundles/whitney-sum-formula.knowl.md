+++
id = "fiber-bundles/whitney-sum-formula"
title = "Whitney sum formula"
kind = "theorem"
summary = "Total characteristic classes multiply when vector bundles are combined by direct sum."
aliases = ["Whitney product formula", "multiplicativity of total characteristic classes"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/characteristic-class", "fiber-bundles/direct-sum-vector-bundle", "fiber-bundles/chern-class", "fiber-bundles/stiefel-whitney-class", "topology/singular-cohomology-group", "topology/cup-product-and-cohomology-ring"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) and \(F\) be [[fiber-bundles/vector-bundle|vector bundles]] over the same paracompact base \(X\). The **Whitney sum formula** states that total [[fiber-bundles/characteristic-class|characteristic classes]] multiply under the [[fiber-bundles/direct-sum-vector-bundle|direct sum]]:
\[
c(E\oplus F)=c(E)\smile c(F)
\]
for complex bundles and [[fiber-bundles/chern-class|total Chern classes]], and
\[
w(E\oplus F)=w(E)\smile w(F)
\]
for real bundles and [[fiber-bundles/stiefel-whitney-class|total Stiefel–Whitney classes]]. The first identity uses [[topology/singular-cohomology-group|integral cohomology]] and the second uses coefficients in \(\mathbb Z/2\). In both cases the multiplication is the [[topology/cup-product-and-cohomology-ring|cup product]].

## Component formulas

Comparing homogeneous terms gives
\[
c_k(E\oplus F)=\sum_{i+j=k}c_i(E)\smile c_j(F),
\qquad
w_k(E\oplus F)=\sum_{i+j=k}w_i(E)\smile w_j(F).
\]
Thus \(c_1(E\oplus F)=c_1(E)+c_1(F)\), while higher components include mixed products. The formulas are the product axioms in the standard characterization of these classes.

## Related characteristic classes

Total [[fiber-bundles/pontryagin-class|Pontryagin classes]] also satisfy
\[
p(E\oplus F)=p(E)\smile p(F).
\]
For oriented even-rank real bundles, compatible product orientations give
\[
e(E\oplus F)=e(E)\smile e(F)
\]
for Euler classes. These identities use their own coefficient rings and degree conventions.

## Examples and consequences

Since \(E\oplus\underline{\mathbb F}^{\,m}\) has the same total characteristic class as \(E\), stable isomorphism preserves Chern, Stiefel–Whitney, and Pontryagin classes. The stable triviality
\[
TS^n\oplus\underline{\mathbb R}\cong\underline{\mathbb R}^{\,n+1}
\]
therefore forces all positive-degree Stiefel–Whitney classes of \(TS^n\) to vanish.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: chapter 4, the Stiefel–Whitney product axiom; §14.4, the product theorem for Chern classes.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: the part on characteristic classes and Whitney sums.
