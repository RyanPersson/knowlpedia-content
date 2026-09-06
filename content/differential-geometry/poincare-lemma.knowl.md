+++
id = "differential-geometry/poincare-lemma"
title = "Poincaré lemma"
kind = "theorem"
summary = "Every closed differential form of positive degree is locally exact."
aliases = ["local exactness of differential forms"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/closed-differential-form", "fiber-bundles/exact-differential-form", "fiber-bundles/smooth-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **Poincaré lemma** states that every [[fiber-bundles/closed-differential-form|closed differential form]] of degree \(k>0\) is locally [[fiber-bundles/exact-differential-form|exact]]. Explicitly, if \(M\) is a [[fiber-bundles/smooth-manifold|smooth manifold]], \(p\in M\), and \(\omega\in\Omega^k(M)\) satisfies \(d\omega=0\), then some open neighborhood \(W\) of \(p\) admits \(\eta\in\Omega^{k-1}(W)\) with \(\omega|_W=d\eta\). Equivalently, on every star-shaped open set \(U\subseteq\mathbb R^n\), each closed form of positive degree is exact. In degree zero, the corresponding statement is that a function with zero differential is locally constant.

## Homotopy operator

For a star-shaped \(U\), radial contraction to the center supplies an operator \(K:\Omega^k(U)\to\Omega^{k-1}(U)\) satisfying
\[
dK+Kd=\operatorname{id}-c^*,
\]
where \(c\) is the constant map to the center. The operator is obtained by contracting the pulled-back form with the interval direction and [[differential-geometry/integration-of-differential-forms|integrating]] in that direction. For \(k>0\), \(c^*=0\), so a closed \(\omega\) obeys \(\omega=d(K\omega)\).

## Local rather than global exactness

The lemma does not say that every closed form on a manifold is globally exact. The angular one-form on \(\mathbb R^2\setminus\{0\}\) is locally exact but represents a nonzero [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology]] class. Global failure to patch local primitives is precisely the information that positive-degree de Rham cohomology records.

## Role in de Rham theory

The lemma says that the [[differential-geometry/de-rham-complex|de Rham complex]] is locally exact in positive degrees. Together with [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|smooth partitions of unity]], this local statement is the key analytic input in the [[differential-geometry/de-rham-theorem|de Rham theorem]].

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, the Poincaré lemma and de Rham theory.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: the chapters on differential forms and de Rham theory.
