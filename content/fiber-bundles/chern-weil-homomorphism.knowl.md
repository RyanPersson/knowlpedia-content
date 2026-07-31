+++
id = "fiber-bundles/chern-weil-homomorphism"
title = "Chern–Weil homomorphism"
kind = "definition"
summary = "The graded-algebra map from invariant polynomials on a Lie algebra to de Rham cohomology."
aliases = ["Chern-Weil map", "Weil homomorphism"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] with [[lie-groups/lie-algebra|Lie algebra \(\mathfrak g\)]], and write
\[
I(G)=\operatorname{Sym}(\mathfrak g^*)^G
\]
for its algebra of [[fiber-bundles/invariant-polynomial-on-a-lie-algebra|invariant polynomials]]. The **Chern–Weil homomorphism** of \(P\) is the graded-algebra map
\[
\operatorname{CW}_P:I(G)\longrightarrow H_{\mathrm{dR}}^{\mathrm{even}}(M),
\qquad
p\longmapsto [p(F_A)],
\]
where \(A\) is any [[fiber-bundles/principal-connection|principal connection]] and \(F_A\) is its curvature. A polynomial of degree \(k\) maps to degree \(2k\). The [[fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection|Chern–Weil theorem]] makes the class independent of \(A\).

## Algebra and naturality

With the standard symmetric-product convention for invariant polynomials,
\[
\operatorname{CW}_P(pq)
=
\operatorname{CW}_P(p)\smile\operatorname{CW}_P(q),
\qquad
\operatorname{CW}_P(1)=1.
\]
The product on the right is the [[topology/cup-product-and-cohomology-ring|cohomology-ring product]], identified with wedge product in [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology]]. If \(f:N\to M\), then
\[
\operatorname{CW}_{f^*P}(p)=f^*\operatorname{CW}_P(p).
\]

## Standard examples

For a [[fiber-bundles/unitary-frame-bundle-reduction|unitary frame bundle]], the coefficients of
\[
\det\!\left(I+\frac{i}{2\pi}F_A\right)
\]
give the real images of [[fiber-bundles/chern-class|Chern classes]]. Trace polynomials on orthogonal bundles produce [[fiber-bundles/pontryagin-class|Pontryagin classes]], and the Pfaffian on an oriented even-rank orthogonal bundle produces the [[fiber-bundles/euler-class|Euler class]].

## Conventions and scope

**Warning.** Normalizing factors such as \(2\pi\), \(i\), and factorials depend on how a polynomial is identified with its polarized multilinear form. The unnormalized homomorphism naturally produces real or complex de Rham classes; proving that a chosen normalization is integral is an additional theorem.

The notation \(\operatorname{CW}_P\) records dependence on the bundle \(P\), even though it does not depend on the auxiliary connection.

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: chapter 11, invariant polynomials and the Chern–Weil homomorphism.
2. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. II, Wiley Classics, 1996. [Publisher record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/mathematics-16ma/geometry-topology-16ma6/foundations-of-differential-geometry-volume-2-978-0-471-15732-8). Relevant: chapter XII, characteristic forms.
