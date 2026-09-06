+++
id = "fiber-bundles/thom-class"
title = "Thom class"
kind = "definition"
summary = "The relative cohomology class that restricts to the orientation generator in every fiber of an oriented vector bundle."
aliases = ["orientation class of a vector bundle", "Thom cohomology class"]
domains = ["fiber-bundles", "topology"]
prerequisites = ["fiber-bundles/orientation-of-a-real-vector-bundle", "fiber-bundles/vector-bundle", "fiber-bundles/zero-section", "topology/singular-cohomology-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\pi:E\to B\) be an [[fiber-bundles/orientation-of-a-real-vector-bundle|oriented]] real [[fiber-bundles/vector-bundle|vector bundle]] of rank \(r\) over a paracompact Hausdorff base, and let \(E^\times=E\setminus 0_E(B)\) be the complement of its [[fiber-bundles/zero-section|zero section]]. The **Thom class** of \(E\) is the unique class
\[
u_E\in H^r(E,E^\times;\mathbb Z)
\]
whose restriction to every fiber pair
\[
(E_b,E_b\setminus\{0_b\})
\cong
(\mathbb R^r,\mathbb R^r\setminus\{0\})
\]
is the generator determined by the chosen fiber orientation. Thus the local orientation generators fit together into one global [[topology/singular-cohomology-group|relative singular cohomology class]].

## Thom isomorphism and naturality

Cup product with \(u_E\) gives the Thom isomorphism
\[
H^q(B;\mathbb Z)
\longrightarrow
H^{q+r}(E,E^\times;\mathbb Z),
\qquad
a\longmapsto \pi^*a\smile u_E,
\]
If \(f:B'\to B\) is a map from another paracompact Hausdorff base, the pullback orientation on \(f^*E\) is characterized by
\[
u_{f^*E}=\widetilde f^{\,*}u_E,
\]
where \(\widetilde f:f^*E\to E\) is the canonical [[fiber-bundles/bundle-map|bundle map]].

## Models and examples

After choosing a [[fiber-bundles/bundle-metric|bundle metric]], excision identifies the defining group with \(H^r(D(E),S(E);\mathbb Z)\), where \(D(E)\) and \(S(E)\) are the disk and [[fiber-bundles/sphere-bundle|sphere bundles]]. For the trivial oriented bundle \(B\times\mathbb R^r\), the Thom class is the exterior product of \(1\in H^0(B;\mathbb Z)\) with the preferred generator of \(H^r(\mathbb R^r,\mathbb R^r\setminus\{0\};\mathbb Z)\).

Pulling \(u_E\) back along the zero section produces the Euler class. More generally, transverse sections represent this class geometrically through their zero loci.

## Coefficients and orientation

Reversing the orientation of \(E\) changes \(u_E\) to \(-u_E\). A nonorientable real bundle has no integral Thom class with the stated fiberwise generator property; its Thom class instead uses the orientation local system. With coefficients in \(\mathbb Z/2\), every real vector bundle has a canonical Thom class because the two signs agree.

**Warning.** The Thom class belongs to relative, or equivalently fiberwise compactly supported, cohomology. Its image in ordinary \(H^r(E;\mathbb Z)\) may lose the support information essential to the definition.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Chapters 9–10, oriented bundles, Thom classes, and the Thom isomorphism.
2. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter 6, Thom isomorphism and characteristic classes.
