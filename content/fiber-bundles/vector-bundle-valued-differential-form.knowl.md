+++
id = "fiber-bundles/vector-bundle-valued-differential-form"
title = "Vector-bundle-valued differential form"
kind = "definition"
summary = "A differential form whose value at each point lies in a specified vector-bundle fiber."
aliases = ["E-valued differential form", "bundle-valued differential form"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/section-of-a-fiber-bundle", "fiber-bundles/vector-field", "fiber-bundles/section-of-a-vector-bundle", "fiber-bundles/differential-k-form"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(E\to M\) be a smooth real or complex [[fiber-bundles/vector-bundle|vector bundle]] and let \(k\geq 0\). An **\(E\)-valued differential \(k\)-form** is a [[fiber-bundles/section-of-a-fiber-bundle|smooth section]]
\[
\omega\in\Omega^k(M;E):=
\Gamma\!\left(\Lambda^kT^*M\otimes E\right).
\]
Equivalently, \(\omega\) assigns to [[fiber-bundles/vector-field|vector fields]] \(X_1,\ldots,X_k\) a section \(\omega(X_1,\ldots,X_k)\) of \(E\), alternatingly and \(C^\infty(M)\)-multilinearly. When \(k=0\), this is simply a [[fiber-bundles/section-of-a-vector-bundle|smooth section of \(E\)]]. When \(E=M\times\mathbb R\), the definition reduces to an ordinary [[fiber-bundles/differential-k-form|differential \(k\)-form]].

## Algebraic structure

A scalar form \(\alpha\in\Omega^p(M)\) and an \(E\)-valued form \(\omega\in\Omega^q(M;E)\) have a wedge product \(\alpha\wedge\omega\in\Omega^{p+q}(M;E)\), obtained by alternating the tensor product. Thus \(\Omega^\bullet(M;E)\) is a [[algebra-modules/graded-module|graded module]] over the algebra \(\Omega^\bullet(M)\).

A [[fiber-bundles/connection-on-a-vector-bundle|connection on \(E\)]] extends the [[fiber-bundles/exterior-derivative|exterior derivative]] to a covariant exterior derivative
\[
d_\nabla:\Omega^k(M;E)\longrightarrow\Omega^{k+1}(M;E).
\]
Unlike the scalar exterior derivative, this operator depends on the chosen connection.

## Local form and pullback

In a local frame \(e_1,\ldots,e_r\) of \(E\), every bundle-valued form has a unique expression
\[
\omega=\sum_{a=1}^r\omega^a\otimes e_a,
\qquad
\omega^a\in\Omega^k(M).
\]
The coefficient forms change with the frame, while \(\omega\) does not. If \(f:N\to M\) is smooth, then ordinary pullback on the form factor and bundle pullback on the value factor give
\[
f^*\omega\in\Omega^k(N;f^*E).
\]
The codomain is \(f^*E\), not \(E\), unless additional bundle data identify them.

## Examples and scope

The [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature of a vector-bundle connection]] is an \(\operatorname{End}(E)\)-valued \(2\)-form. On a principal bundle, tensorial adjoint-valued forms descend to forms on the base with values in the [[fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action|adjoint bundle]]. These are instances of the same construction, but a Lie-algebra-valued form on the total space is not automatically a bundle-valued form on the base.

**Warning.** For a [[fiber-bundles/complex-vector-bundle|complex vector bundle]] over a real manifold, authors may write either \(\Lambda^kT^*M\otimes_{\mathbb R}E\) or its canonically equivalent complexified formulation. The scalar convention should be stated when complex conjugation or forms of type \((p,q)\) enter.

## References

1. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume I, Wiley Classics, 1996. [Publisher record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/mathematics-16ma/geometry-topology-16ma6/foundations-of-differential-geometry-volume-1-978-0-471-15733-5). Relevant: Chapter II, tensorial forms and covariant differentiation.
2. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter I, vector-bundle-valued differential forms.
