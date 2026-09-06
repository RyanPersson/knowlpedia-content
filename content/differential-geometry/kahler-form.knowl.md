+++
id = "differential-geometry/kahler-form"
title = "Kähler form"
kind = "definition"
summary = "A closed real positive form of type one-one on a complex manifold."
aliases = ["fundamental form of a Kähler metric"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/symplectic-manifold"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,J)\) be a [[differential-geometry/complex-manifold|complex manifold]]. A **Kähler form** is a real differential \(2\)-form \(\omega\) such that
\[
d\omega=0,\qquad \omega(JX,JY)=\omega(X,Y),\qquad
\omega(X,JX)>0
\]
for every nonzero real tangent vector \(X\). The second condition says that \(\omega\) has complex type \((1,1)\), and the third is positivity. These conditions make \(\omega\) nondegenerate, so it defines a [[differential-geometry/symplectic-manifold|symplectic manifold]] structure on \(M\). The formula
\[
g(X,Y)=\omega(X,JY)
\]
defines a \(J\)-invariant Riemannian metric, called the associated Kähler metric.

## Equivalent metric formulation

Conversely, the [[differential-geometry/fundamental-form-almost-hermitian|fundamental form]] \(\omega(X,Y)=g(JX,Y)\) of a [[fiber-bundles/hermitian-metric|Hermitian metric]] is a Kähler form exactly when it is closed. Thus specifying a Kähler form on \((M,J)\) is equivalent to specifying a [[differential-geometry/kahler-metric|Kähler metric]], and it makes \((M,J,g)\) a [[differential-geometry/kahler-manifold|Kähler manifold]].

## Local potentials

Every Kähler form is locally expressible as
\[
\omega=i\,\partial\bar\partial\varphi
\]
for a real strictly plurisubharmonic function \(\varphi\), with a constant factor changed under other \(d^c\) conventions. Adding the real part of a holomorphic function to \(\varphi\) does not change \(\omega\). This potential description is local; a global potential need not exist.

## Examples and conventions

The standard form \(\frac{i}{2}\sum_j dz^j\wedge d\bar z^j\) on \(\mathbb C^n\) is Kähler, as is the Fubini–Study form on [[algebraic-geometry-foundations/projective-space|complex projective space]]. Some authors use \(\omega(X,Y)=g(X,JY)\), which reverses the sign relative to the convention here and therefore changes the corresponding positivity inequality.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §3.1, Kähler metrics and forms.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Chapter 3, Kähler forms and local potentials.
