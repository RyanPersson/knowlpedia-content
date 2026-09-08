+++
id = "fiber-bundles/thom-class"
title = "Thom class"
kind = "definition"
summary = "The relative cohomology class that restricts to the orientation generator in every fiber of an oriented vector bundle."
aliases = ["orientation class of a vector bundle", "Thom cohomology class"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/topological-real-vector-bundle", "topology/relative-singular-cohomology-group", "algebra-rings/commutative-ring", "fiber-bundles/paracompact-topological-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:E\to B\) be a rank-\(r\) [[fiber-bundles/topological-real-vector-bundle|topological real vector bundle]] over a paracompact Hausdorff base, let \(R\) be a commutative ring with identity, and write \(E^\times=E\setminus\{0_b:b\in B\}\). An \(R\)-orientation is a choice of generator of the free rank-one \(R\)-module \(H^r(E_b,E_b\setminus\{0_b\};R)\) in each fiber, locally compatible under bundle trivializations.

Given this orientation, the **Thom class** is the unique [[topology/relative-singular-cohomology-group|relative singular cohomology class]]
\[
u_E\in H^r(E,E^\times;R)
\]
whose restriction to every fiber pair is the chosen generator. For \(R=\mathbb Z\) and \(r>0\), the choice is the ordinary continuous orientation of the real fibers. For \(r=0\), the canonical orientation chooses \(1\), and \(u_E=1\in H^0(B;R)\).

## Thom isomorphism and naturality

Cup product with \(u_E\) gives the Thom isomorphism
\[
H^q(B;R)
\longrightarrow
H^{q+r}(E,E^\times;R),
\qquad
a\longmapsto \pi^*a\smile u_E,
\]
If \(f:B'\to B\) is a map from another paracompact Hausdorff base, the pullback orientation on \(f^*E\) is characterized by
\[
u_{f^*E}=\widetilde f^{\,*}u_E,
\]
where \(\widetilde f:f^*E\to E\) is the canonical continuous bundle map, and \(f\) is continuous.

## Models and examples

After choosing a continuous positive-definite fiber metric, excision identifies the defining group with \(H^r(D(E),S(E);R)\), where \(D(E)=\{v:\|v\|\le1\}\) and \(S(E)=\{v:\|v\|=1\}\) are the disk and unit sphere bundles. For the trivial oriented bundle \(B\times\mathbb R^r\), the Thom class is the exterior product of \(1\in H^0(B;R)\) with the preferred generator of \(H^r(\mathbb R^r,\mathbb R^r\setminus\{0\};R)\).

With integral coefficients, pulling \(u_E\) back along the zero section produces the Euler class. More generally, transverse sections represent this class geometrically through their zero loci.

## Coefficients and orientation

Reversing the orientation of \(E\) changes \(u_E\) to \(-u_E\). A nonorientable real bundle has no integral Thom class with the stated fiberwise generator property; its Thom class instead uses the orientation local system. With coefficients in \(\mathbb Z/2\), every real vector bundle has a canonical Thom class because the two signs agree.

**Warning.** The Thom class belongs to relative, or equivalently fiberwise compactly supported, cohomology. Its image in ordinary \(H^r(E;\mathbb Z)\) may lose the support information essential to the definition.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Chapters 9–10, oriented bundles, Thom classes, and the Thom isomorphism.
2. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter 6, Thom isomorphism and characteristic classes.
