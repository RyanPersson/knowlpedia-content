+++
id = "fiber-bundles/quaternionic-vector-bundle"
title = "Quaternionic vector bundle"
kind = "definition"
summary = "A vector bundle locally modeled on a finite-dimensional right module over the quaternion division algebra."
aliases = ["quaternionic bundle", "quaternion vector bundle"]
domains = ["fiber-bundles", "linear-algebra"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. A
**quaternionic vector bundle of rank \(n\)** over \(M\) is a
[[fiber-bundles/vector-bundle|smooth vector bundle]]
\(\pi:E\to M\) whose fibers are right modules over the
[[linear-algebra/quaternion-division-algebra|quaternion division algebra]]
\(\mathbb H\), together with [[fiber-bundles/local-trivialization|local trivializations]]
\[
\Phi_\alpha:E|_{U_\alpha}\longrightarrow U_\alpha\times\mathbb H^n
\]
that are right \(\mathbb H\)-linear on every fiber. Equivalently, its
[[fiber-bundles/transition-function|transition functions]] are [[fiber-bundles/smooth-map|smooth maps]] into
\(\operatorname{GL}(n,\mathbb H)\). Its underlying real vector bundle has
rank \(4n\). [[fiber-bundles/bundle-morphism|Bundle morphisms]] in this category are smooth, fiberwise right
\(\mathbb H\)-linear maps.

## Equivalent complex description

Restricting scalars along \(\mathbb C\subset\mathbb H\) turns \(E\) into a
[[fiber-bundles/complex-vector-bundle|complex vector bundle]] of rank \(2n\).
Right multiplication by \(j\) defines an antilinear [[fiber-bundles/bundle-map|bundle map]] \(J:E\to E\)
satisfying \(J^2=-I\). Conversely, such a pair \((E,J)\) recovers the right
quaternionic action. This is the standard complex description of a quaternion
bundle.

## Metrics and examples

A fiberwise quaternionic [[fiber-bundles/hermitian-metric|Hermitian metric]] reduces the transition functions
from \(\operatorname{GL}(n,\mathbb H)\) to the
[[lie-groups/compact-symplectic-group|compact symplectic group]]
\(\operatorname{Sp}(n)\). Such a metric can be assembled from local standard
metrics by a smooth partition of unity. The product
\(M\times\mathbb H^n\) is the trivial example, while the tautological line
bundle over quaternionic projective space is the basic nontrivial example.

## Conventions and near-misses

**Warning.** Some authors call a rank-three subbundle of
\(\operatorname{End}_{\mathbb R}(E)\), locally spanned by endomorphisms
satisfying the quaternion relations, a “quaternionic structure.” That weaker
datum need not choose a global right \(\mathbb H\)-module structure. Likewise,
an antilinear map with square \(+I\) defines a real structure, not a
quaternionic vector bundle.

## References

1. M. F. Atiyah, *K-Theory*, lecture notes by D. W. Anderson, W. A. Benjamin, 1967. [Author-hosted scan](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahk.pdf). Relevant: §1.5 on quaternion bundles as complex bundles with an antilinear map squaring to \(-I\).
2. D. Husemoller, *Fibre Bundles*, 3rd ed., Graduate Texts in Mathematics 20, Springer, 1994. [Publisher record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapters 2–3 on vector bundles, transition functions, and reduction of structure group.
