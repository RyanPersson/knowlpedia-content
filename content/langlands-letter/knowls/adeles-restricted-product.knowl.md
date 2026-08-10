+++
id = "langlands-letter/knowls/adeles-restricted-product"
title = "Adeles and restricted products"
kind = "definition"
summary = "The locally compact restricted product of all completions of a global field."
aliases = ["adeles-restricted-product", "Adeles and Restricted Products"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/adeles-restricted-product.md"
section_mode = "progressive"
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|global field]]. For
each nonarchimedean place \(v\), let
\(\mathcal O_v\subset F_v\) be the
[[algebra-fields-galois/valuation-ring|valuation ring]]. The **finite adele
ring**
is the restricted product

\[
\mathbb A_{F,f}
=
\prod_{v\nmid\infty}'F_v
=
\left\{
(x_v)_v:x_v\in\mathcal O_v
\text{ for all but finitely many }v
\right\}.
\]

For a [[langlands-letter/knowls/global-local-fields-completions|number
field]],

\[
\mathbb A_F
=
\left(\prod_{v\mid\infty}F_v\right)
\times\mathbb A_{F,f}.
\]

A [[langlands-letter/knowls/global-local-fields-completions|global function
field]] has no archimedean places, so its full adele ring is
the corresponding restricted product over all [[algebraic-geometry-foundations/closed-point|closed points]] of its curve.

## Restricted-product topology

A basic open set is a product \(\prod_v U_v\), where \(U_v\subset F_v\) is
open and \(U_v=\mathcal O_v\) for all but finitely many \(v\). This topology
makes \(\mathbb A_F\) a [[topology/locally-compact-space|locally compact]] topological ring. It is not the
[[topology/subspace-topology|subspace topology]] inherited from the unrestricted direct product.

## Global diagonal

The diagonal embedding \(F\hookrightarrow\mathbb A_F\) has discrete image,
and the additive quotient \(\mathbb A_F/F\) is compact. These facts underlie
adelic Fourier analysis and the product formula.

For an [[algebraic-geometry-foundations/algebraic-group|algebraic group]] \(G\), its adelic points are themselves a restricted
product, using integral models or
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial
subgroups]] at almost all
places. [[langlands/automorphic-form|Automorphic forms]] then live on
\(G(F)\backslash G(\mathbb A_F)\).

## Measures

A restricted product of local [[harmonic-analysis/haar-measure|Haar measures]] requires almost-all
normalizations, often \(\operatorname{vol}(\mathcal O_v)=1\).
[[langlands/tamagawa-measure|Tamagawa measures]] incorporate convergence
factors and are additional global data;
they are not automatic from the set-theoretic restricted product.

## References

1. John Tate, “Fourier analysis in number fields and Hecke's zeta
   functions,” in *Algebraic Number Theory*, 1967.
2. André Weil, *Basic Number Theory*, Springer, 1967.
