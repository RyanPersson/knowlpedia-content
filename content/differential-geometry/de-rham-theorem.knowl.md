+++
id = "differential-geometry/de-rham-theorem"
title = "de Rham theorem"
kind = "theorem"
summary = "Integration identifies de Rham cohomology naturally with singular cohomology with real coefficients."
aliases = ["de Rham isomorphism theorem"]
domains = ["differential-geometry", "topology"]
section_mode = "progressive"
+++

For every [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\), [[differential-geometry/integration-of-differential-forms|integration]] over smooth singular simplices defines a cochain map
\[
\mathcal I:\Omega^k(M)\longrightarrow C_{\mathrm{sm}}^k(M;\mathbb R),
\qquad
\mathcal I(\omega)(\sigma)=\int_{\Delta^k}\sigma^*\omega.
\]
The **de Rham theorem** states that the induced map
\[
H_{\mathrm{dR}}^k(M)\xrightarrow{\;\cong\;}H^k(M;\mathbb R)
\]
is an isomorphism for every \(k\). Thus the cohomology of the [[differential-geometry/de-rham-complex|de Rham complex]] of smooth forms agrees naturally with [[topology/singular-cohomology-group|singular cohomology]] with real coefficients. No orientation or compactness assumption on \(M\) is required.

## Naturality and products

For a [[fiber-bundles/smooth-map|smooth map]] \(f:M\to N\), [[fiber-bundles/pullback-of-differential-forms|pullback of forms]] and pullback of singular cochains commute with the de Rham isomorphism. On cohomology, the isomorphism also identifies [[fiber-bundles/wedge-product-of-differential-forms|wedge products of forms]] with cup products, so it is an isomorphism of graded real algebras, not merely of graded [[linear-algebra/vector-space|vector spaces]].

## Proof architecture

One proof uses the [[differential-geometry/poincare-lemma|Poincaré lemma]] to establish local exactness and [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]] to pass from local to global information. Another proceeds by showing that both theories satisfy compatible [[differential-geometry/mayer-vietoris-sequence-for-de-rham-cohomology|Mayer–Vietoris sequences]], checking the result on contractible coordinate neighborhoods, and then gluing. Smooth singular cochains compute the same cohomology as ordinary singular cochains.

## Coefficients and compact supports

The target is real singular cohomology. The theorem does not identify de Rham cohomology with integral cohomology: torsion information disappears over \(\mathbb R\). There is a separate compact-support version relating [[differential-geometry/compactly-supported-de-rham-cohomology|compactly supported de Rham cohomology]] to singular cohomology with compact supports; its support conditions should not be silently inserted into the ordinary theorem.

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, the de Rham theorem, products, and Mayer–Vietoris method.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: the chapter on de Rham theory.
