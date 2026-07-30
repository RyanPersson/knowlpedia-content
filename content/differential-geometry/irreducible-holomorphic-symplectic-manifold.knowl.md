+++
id = "differential-geometry/irreducible-holomorphic-symplectic-manifold"
title = "Irreducible holomorphic symplectic manifold"
kind = "definition"
summary = "A compact simply connected Kähler manifold whose holomorphic two-forms are spanned by an everywhere nondegenerate form."
aliases = ["IHS manifold", "compact hyperkähler manifold in the complex-geometric sense"]
domains = ["differential-geometry", "complex-geometry"]
section_mode = "progressive"
+++

An **irreducible holomorphic symplectic manifold** is a compact, simply connected [[differential-geometry/kahler-manifold|Kähler manifold]] \(X\) such that
\[
H^0(X,\Omega_X^2)=\mathbb C\sigma
\]
for an everywhere nondegenerate holomorphic \(2\)-form \(\sigma\). Thus \(X\) is a [[differential-geometry/holomorphic-symplectic-manifold|holomorphic symplectic manifold]], its complex dimension is even, and every global holomorphic \(2\)-form is a scalar multiple of \(\sigma\). The form is determined only up to nonzero scalar unless it is included as part of the data. Compactness, simple connectedness, and the one-dimensionality condition are all essential to this convention.

## Riemannian interpretation

Yau’s theorem gives a Ricci-flat
[[differential-geometry/kahler-metric|Kähler metric]] in each
[[differential-geometry/kahler-class|Kähler class]]. If
\(\dim_{\mathbb C}X=2n\), the IHS conditions imply that the restricted
holonomy of this metric is \(\operatorname{Sp}(n)\). Because \(X\) is simply
connected, its full and restricted holonomy groups agree, so the full
holonomy is also \(\operatorname{Sp}(n)\). This is why these manifolds are
often called compact
[[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]] in
complex geometry [Huybrechts, §1](https://doi.org/10.1007/s002220050280).
The terminology packages a
[[differential-geometry/complex-manifold|complex manifold]], whereas a
Riemannian hyperkähler structure includes a particular metric and
quaternionic triple of complex structures.

## Examples and non-examples

A K3 surface is the basic two-dimensional example. Hilbert schemes of points on a K3 surface and generalized Kummer varieties provide higher-dimensional families [Beauville, §§5–6](https://doi.org/10.4310/jdg/1214438181). A complex symplectic torus is compact and Kähler but not simply connected. A product of two K3 surfaces is simply connected and holomorphic symplectic, but its space of holomorphic \(2\)-forms has dimension two, so it is not irreducible in this sense.

## Conventions and scope

“Compact hyperkähler,” “irreducible symplectic,” and “irreducible holomorphic symplectic” are not used uniformly. Some authors replace simple connectedness by an irreducibility or holonomy condition; in the compact Kähler setting these standard formulations are closely related but should not be transferred unchanged to noncompact manifolds. The word “irreducible” here is not algebraic irreducibility of the underlying analytic space.

## References

1. Arnaud Beauville, “Variétés Kähleriennes dont la première classe de Chern est nulle,” *Journal of Differential Geometry* 18 (1983), 755–782. [DOI record](https://doi.org/10.4310/jdg/1214438181). Relevant: §§3–6, decomposition, irreducible symplectic factors, and standard examples.
2. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, definitions, terminology, and the holonomy interpretation.
