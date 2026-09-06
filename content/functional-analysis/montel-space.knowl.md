+++
id = "functional-analysis/montel-space"
title = "Montel space"
kind = "definition"
summary = "A barreled locally convex space in which every closed bounded subset is compact."
aliases = ["Montel locally convex space"]
domains = ["functional-analysis"]
prerequisites = ["functional-analysis/barreled-space", "functional-analysis/bounded-subset-tvs", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **Montel space** is a Hausdorff [[functional-analysis/barreled-space|barreled locally convex space]] \(E\) in which every closed [[functional-analysis/bounded-subset-tvs|bounded subset]] is compact. Equivalently, every bounded subset of \(E\) has compact closure. Both clauses matter: relative compactness of bounded sets is the compactness condition, while barreledness supplies the uniform-boundedness behavior expected of the space. Compactness and boundedness refer to the given locally convex topology; changing that topology can therefore change whether the same underlying [[linear-algebra/vector-space|vector space]] is Montel.

## Structural consequences

Every Montel space is complete and reflexive as a [[functional-analysis/locally-convex-space|locally convex space]]: the canonical map into the strong bidual is a topological isomorphism. Bounded sets have strong compactness properties, so bounded nets possess convergent subnets after taking closure. These results combine the semi-Montel compactness condition with barreledness.

## Examples and non-examples

Finite-dimensional Hausdorff locally convex spaces are Montel. The [[functional-analysis/schwartz-space|Schwartz space]] \(\mathcal S(\mathbb R^n)\) and standard spaces of smooth functions are fundamental infinite-dimensional examples; more generally, [[functional-analysis/nuclear-space|nuclear]] [[functional-analysis/frechet-space|Fréchet spaces]] are Montel. No infinite-dimensional [[linear-algebra/banach-space|Banach space]] is Montel, because its closed unit ball is bounded but is compact only in finite dimension.

## Conventions and nearby notions

A **semi-Montel space** is a locally convex space in which every bounded set is relatively compact, without the barreledness requirement. Some sources fold completeness or additional separation assumptions into their terminology; the definition here follows the standard Hausdorff, barreled formulation. Montel spaces should not be confused with Montel families of holomorphic functions, although the compactness principle behind the names is closely related.

## References

1. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter IV, §6 on Montel and Schwartz spaces.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967; Dover reprint, 2006. [Dover publisher record](https://store.doverpublications.com/products/9780486453521). Relevant: Chapter 34 on Montel spaces.
