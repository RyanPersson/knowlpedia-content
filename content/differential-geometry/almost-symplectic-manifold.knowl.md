+++
id = "differential-geometry/almost-symplectic-manifold"
title = "Almost symplectic manifold"
kind = "definition"
summary = "A smooth manifold equipped with a pointwise nondegenerate two-form, without a closedness requirement."
aliases = ["nondegenerate 2-form manifold"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/differential-k-form", "differential-geometry/tangent-space", "differential-geometry/symplectic-vector-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

An **almost symplectic manifold** is a pair \((M,\omega)\), where \(M\) is a finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] and \(\omega\) is a smooth [[fiber-bundles/differential-k-form|differential \(2\)-form]] such that \(\omega_p\) is nondegenerate at every \(p\in M\). Thus
\[
\omega_p(v,w)=0\text{ for every }w\in T_pM
\quad\Longrightarrow\quad v=0.
\]
Equivalently, each [[differential-geometry/tangent-space|tangent space]] \((T_pM,\omega_p)\) is a [[differential-geometry/symplectic-vector-space|symplectic vector space]]. Closedness is not required: an almost symplectic form may have \(d\omega\ne0\). Requiring \(d\omega=0\) gives a [[differential-geometry/symplectic-manifold|symplectic manifold]].

## Structure and consequences

Nondegeneracy forces \(M\) to have even dimension, say \(2n\). The top-degree form \(\omega^n\) is nowhere zero, so \(\omega\) canonically orients \(M\). These are pointwise consequences of symplectic linear algebra; they do not use \(d\omega=0\).

The [[fiber-bundles/bundle-map|bundle map]]
\[
\omega^\flat:TM\longrightarrow T^*M,\qquad
v\longmapsto\iota_v\omega
\]
is a vector-bundle isomorphism. Consequently every one-form determines a unique [[fiber-bundles/vector-field|vector field]] through contraction with \(\omega\), even when the form is not closed.

## Examples and non-examples

Every symplectic manifold is almost symplectic after forgetting closedness. On \(\mathbb R^4\), let
\[
\omega=dx_1\wedge dx_2+e^{x_1}dx_3\wedge dx_4.
\]
Its square is \(2e^{x_1}dx_1\wedge dx_2\wedge dx_3\wedge dx_4\), so it is nondegenerate, while
\[
d\omega=e^{x_1}dx_1\wedge dx_3\wedge dx_4\ne0.
\]
Thus it is almost symplectic but not symplectic. An odd-dimensional manifold is a decisive non-example because an alternating form on an odd-dimensional tangent space is necessarily degenerate.

## Conventions and scope

Some authors use “nondegenerate \(2\)-form” without naming the resulting structure, while others reserve “almost symplectic” for this precise pointwise condition. The word “almost” records only the missing closedness axiom; it does not specify an [[differential-geometry/almost-complex-structure|almost complex structure]], although compatible almost complex structures can be constructed from such a form.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Oxford DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 2, nondegenerate skew forms, and Chapter 3, symplectic forms.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: pp. 3–8, nondegenerate and closed \(2\)-forms.
