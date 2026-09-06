+++
id = "differential-geometry/compactly-supported-de-rham-cohomology"
title = "Compactly supported de Rham cohomology"
kind = "definition"
summary = "The cohomology of the de Rham complex restricted to compactly supported differential forms."
aliases = ["de Rham cohomology with compact support", "compact-support de Rham cohomology"]
domains = ["differential-geometry", "topology"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/exterior-derivative", "differential-geometry/compactly-supported-differential-form", "differential-geometry/de-rham-complex"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. Because the [[fiber-bundles/exterior-derivative|exterior derivative]] does not enlarge support, the spaces of [[differential-geometry/compactly-supported-differential-form|compactly supported differential forms]] form the subcomplex
\[
0\longrightarrow\Omega_c^0(M)\xrightarrow{d}\Omega_c^1(M)\xrightarrow{d}\cdots
\]
of the [[differential-geometry/de-rham-complex|de Rham complex]]. The **compactly supported de Rham cohomology** of \(M\) is
\[
H_{c,\mathrm{dR}}^k(M)
=\frac{\ker(d:\Omega_c^k(M)\to\Omega_c^{k+1}(M))}
{\operatorname{im}(d:\Omega_c^{k-1}(M)\to\Omega_c^k(M))}.
\]
Thus a class is represented by a closed compactly supported \(k\)-form, and two representatives agree when their difference is the exterior derivative of a compactly supported \((k-1)\)-form.

## Functoriality and support

If \(f:M\to N\) is a [[differential-geometry/proper-smooth-map|proper smooth map]], pullback preserves compact support and induces \(f^*:H_{c,\mathrm{dR}}^k(N)\to H_{c,\mathrm{dR}}^k(M)\). Arbitrary [[fiber-bundles/smooth-map|smooth maps]] need not do so. If \(j:U\hookrightarrow M\) is an open inclusion, extension by zero sends compactly supported forms on \(U\) to compactly supported forms on \(M\); smoothness holds because each support is closed away from the boundary of \(U\).

## Duality and examples

For an oriented \(n\)-manifold, wedge product followed by [[differential-geometry/integration-of-differential-forms|integration]] gives the Poincaré pairing
\[
H_{c,\mathrm{dR}}^k(M)\times H_{\mathrm{dR}}^{n-k}(M)\longrightarrow\mathbb R.
\]
Its nondegeneracy is the compact-support form of Poincaré duality. If \(M\) is compact, compactly supported and ordinary de Rham cohomology coincide. For \(\mathbb R^n\), only the top-degree compactly supported group is nonzero, and integration identifies it with \(\mathbb R\).

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, compact supports and Poincaré duality.
2. Glen E. Bredon, *Topology and Geometry*, Springer, 1993. [DOI record](https://doi.org/10.1007/978-1-4757-6848-0). Relevant: Chapter VI, de Rham theory and compact supports.
