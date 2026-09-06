+++
id = "differential-geometry/integration-of-differential-forms"
title = "Integration of differential forms"
kind = "definition"
summary = "Integration assigns a real number to a compactly supported top-degree form on an oriented manifold."
aliases = ["integral of a top form", "integration on a manifold"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/orientation-of-a-smooth-manifold", "fiber-bundles/smooth-manifold", "differential-geometry/compactly-supported-differential-form", "fiber-bundles/differential-k-form", "fiber-bundles/partition-of-unity-subordinate-to-an-open-cover"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be an [[differential-geometry/orientation-of-a-smooth-manifold|oriented]] \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]]. The **integral** of a [[differential-geometry/compactly-supported-differential-form|compactly supported]] [[fiber-bundles/differential-k-form|differential \(n\)-form]] \(\omega\) is the number obtained by choosing an orientation-preserving atlas and a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|subordinate partition of unity]] \((\rho_i)\), writing
\[
(x_i^{-1})^*(\rho_i\omega)=f_i\,dx^1\wedge\cdots\wedge dx^n,
\]
and setting
\[
\int_M\omega=\sum_i\int_{x_i(U_i)}f_i(x)\,dx.
\]
Compact support makes only finitely many terms relevant after a suitable locally finite choice, and the change-of-variables theorem makes the result independent of all choices.

## Basic properties

Integration is linear. Reversing the orientation of \(M\) changes the sign of every integral. If \(F:M\to N\) is an orientation-preserving [[fiber-bundles/diffeomorphism|diffeomorphism]] of oriented \(n\)-manifolds and \(\omega\) is compactly supported on \(N\), then
\[
\int_M F^*\omega=\int_N\omega.
\]
This change-of-variables identity is the coordinate independence built into the definition.

## Forms of lower degree

A \(k\)-form is not integrated over all of an \(n\)-manifold when \(k\ne n\). Instead, if \(S\) is an oriented \(k\)-manifold and \(f:S\to M\) is a smooth parametrization for which the integral is defined, one sets
\[
\int_f\omega:=\int_S f^*\omega.
\]
This formulation includes integration over oriented submanifolds and smooth singular simplices.

## Stokes' theorem and cohomology

The compatibility between integration and the [[fiber-bundles/exterior-derivative|exterior derivative]] is [[differential-geometry/stokes-theorem|Stokes' theorem]]:
\[
\int_M d\eta=\int_{\partial M}\eta
\]
with the induced [[differential-geometry/boundary-orientation|boundary orientation]] and appropriate compact-support hypotheses. Consequently, integrals of closed forms over cycles depend only on cohomology and homology classes; this pairing underlies the [[differential-geometry/de-rham-theorem|de Rham theorem]].

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: the chapters on orientations, integration on manifolds, and Stokes' theorem.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: the chapter on integration.
