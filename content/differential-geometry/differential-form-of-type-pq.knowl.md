+++
id = "differential-geometry/differential-form-of-type-pq"
title = "Differential form of type (p,q)"
kind = "definition"
summary = "A complex differential form whose covector factors have a fixed holomorphic and antiholomorphic bidegree."
aliases = ["(p,q)-form", "form of bidegree (p,q)", "complex differential form of type (p,q)"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/complexified-tangent-bundle-splitting", "fiber-bundles/section-of-a-fiber-bundle", "fiber-bundles/wedge-product-of-differential-forms"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[differential-geometry/complex-manifold|complex manifold]], with the [[differential-geometry/complexified-tangent-bundle-splitting|type decomposition]] \(T_{\mathbb C}^*M=T^{*1,0}M\oplus T^{*0,1}M\). A **differential form of type \((p,q)\)** is a [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] of
\[
\Lambda^{p,q}T^*M
=\Lambda^pT^{*1,0}M\otimes\Lambda^qT^{*0,1}M
\subseteq \Lambda^{p+q}T_{\mathbb C}^*M.
\]
Equivalently, it is locally a sum of [[fiber-bundles/wedge-product-of-differential-forms|wedge products]] containing exactly \(p\) holomorphic covector factors and \(q\) antiholomorphic covector factors. Its total degree is \(p+q\); by convention the space is zero if either index is negative or exceeds the complex dimension of \(M\).

## Type decomposition

Every complex-valued \(k\)-form decomposes uniquely as
\[
\alpha=\sum_{p+q=k}\alpha^{p,q},
\qquad
\alpha^{p,q}\in\Omega^{p,q}(M).
\]
Thus \(\Omega^k(M;\mathbb C)=\bigoplus_{p+q=k}\Omega^{p,q}(M)\). The wedge product respects bidegree:
\(\Omega^{p,q}\wedge\Omega^{r,s}\subseteq\Omega^{p+r,q+s}\).

## Local coordinates and conjugation

In holomorphic coordinates \(z^1,\ldots,z^n\), a \((p,q)\)-form is a sum of terms
\[
f_{I\bar J}\,dz^{i_1}\wedge\cdots\wedge dz^{i_p}
\wedge d\bar z^{j_1}\wedge\cdots\wedge d\bar z^{j_q}.
\]
Complex conjugation exchanges bidegrees: \(\overline{\Omega^{p,q}}=\Omega^{q,p}\). Consequently, a real complex-valued form can be of pure type only when its type is fixed by this exchange or when it is zero.

## Relation to complex geometry

The [[differential-geometry/dolbeault-operators|Dolbeault operators]] split the [[fiber-bundles/exterior-derivative|exterior derivative]] according to this bidegree. The pointwise decomposition itself only requires an [[differential-geometry/almost-complex-structure|almost-complex structure]], but holomorphic coordinates and the two-term decomposition of the exterior derivative require [[differential-geometry/integrable-almost-complex-structure|integrability]].

## References

1. C. Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge University Press, 2002. [DOI record](https://doi.org/10.1017/CBO9780511615344). Relevant: §2.1, forms of type \((p,q)\).
2. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter I, §§2–3.
