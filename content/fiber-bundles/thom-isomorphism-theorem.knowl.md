+++
id = "fiber-bundles/thom-isomorphism-theorem"
title = "Thom isomorphism theorem"
kind = "theorem"
summary = "Cup product with the Thom class shifts the cohomology of a bundle base into the relative cohomology of its total space."
aliases = ["Thom isomorphism", "Thom-Gysin isomorphism"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
+++

Let \(\pi:E\to B\) be an \(R\)-oriented real [[fiber-bundles/vector-bundle|vector bundle]] of rank \(r\) over a paracompact Hausdorff base, and let \(E^\times=E\setminus 0_E(B)\). If
\[
u_E\in H^r(E,E^\times;R)
\]
is its [[fiber-bundles/thom-class|Thom class]], then for every \(q\) the map
\[
\Phi_E:H^q(B;R)\longrightarrow H^{q+r}(E,E^\times;R),
\qquad
a\longmapsto \pi^*a\smile u_E,
\]
is an isomorphism. This is the **Thom isomorphism theorem**. It is natural for orientation-preserving pullbacks of vector bundles and sends \(1\in H^0(B;R)\) to \(u_E\).

## Equivalent models

After choosing a [[fiber-bundles/bundle-metric|bundle metric]], excision identifies
\[
H^*(E,E^\times;R)\cong H^*(D(E),S(E);R),
\]
where \(D(E)\) and \(S(E)\) are the disk and [[fiber-bundles/sphere-bundle|sphere bundles]]. Collapsing \(S(E)\) gives the reduced cohomology of the Thom space. These models express the same isomorphism with different support conventions [Milnor–Stasheff, chapter 10](https://doi.org/10.1515/9781400881826).

## Consequences

Pulling \(u_E\) back along the [[fiber-bundles/zero-section|zero section]] gives the [[fiber-bundles/euler-class-as-zero-section|Euler class]]. The theorem also yields Gysin maps and the Gysin long exact sequence of the [[fiber-bundles/sphere-bundle|sphere bundle]]. For the trivial oriented bundle \(B\times\mathbb R^r\), \(\Phi_E\) is the suspension-type degree shift obtained by multiplying with the preferred generator of \(H^r(\mathbb R^r,\mathbb R^r\setminus\{0\};R)\).

## Coefficients and scope

Integral coefficients require an orientation. Every real [[fiber-bundles/vector-bundle|vector bundle]] is orientable over \(\mathbb Z/2\), so the mod-\(2\) theorem has no orientability hypothesis. More generally, a nonorientable bundle admits a Thom isomorphism with its orientation local system.

**Warning.** [[topology/singular-cohomology-group|Ordinary cohomology]] of \(E\) does not retain the fiberwise support encoded by the relative group.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: chapters 9–10, orientations, Thom classes, and the Thom isomorphism theorem.
2. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: chapter 6, Thom isomorphism and Euler class.
