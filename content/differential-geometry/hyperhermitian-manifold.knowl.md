+++
id = "differential-geometry/hyperhermitian-manifold"
title = "Hyper-Hermitian manifold"
kind = "definition"
summary = "A hypercomplex manifold with a Riemannian metric Hermitian for all three complex structures."
aliases = ["hyperhermitian manifold", "hyper-Hermitian metric"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

A **hyper-Hermitian manifold** is a [[differential-geometry/hypercomplex-manifold|hypercomplex manifold]] \((M,I,J,K)\) together with a [[differential-geometry/riemannian-manifold|Riemannian metric]] \(g\) that is Hermitian for each member of the hypercomplex triple:
\[
g(IX,IY)=g(JX,JY)=g(KX,KY)=g(X,Y)
\]
for all tangent vectors \(X,Y\) at the same point. Equivalently, every complex structure \(aI+bJ+cK\) with \(a^2+b^2+c^2=1\) is orthogonal for \(g\). The triple \((I,J,K)\) and metric \(g\) are chosen data. No closedness or parallelism condition is imposed on the associated fundamental two-forms, so hyper-Hermitian is strictly weaker than hyperkähler.

## Associated two-forms

The metric determines three real two-forms
\[
\omega_I(X,Y)=g(IX,Y),\qquad
\omega_J(X,Y)=g(JX,Y),\qquad
\omega_K(X,Y)=g(KX,Y).
\]
They encode the same pointwise compatibility as the metric, but they need not be closed. The structure is hyperkähler precisely when all three forms are closed; equivalently, the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] preserves \(I,J,K\).

## Examples and scope

Quaternionic [[linear-algebra/euclidean-space|Euclidean space]] \(\mathbb H^n\), with its flat metric and complex structures given by multiplication by \(i,j,k\), is hyper-Hermitian and in fact hyperkähler. More generally, every [[differential-geometry/hyperkahler-manifold|hyperkähler manifold]] is hyper-Hermitian after forgetting the closedness of its three [[differential-geometry/kahler-form|Kähler forms]].

A hypercomplex manifold equipped with a Riemannian metric that is Hermitian only for \(I\) is a near miss: invariance under \(J\) and \(K\) is part of the definition and does not follow from invariance under one complex structure.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [Oxford DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapter 7, hyperkähler structures and their underlying hyper-Hermitian data.
