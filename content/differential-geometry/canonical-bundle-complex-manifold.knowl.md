+++
id = "differential-geometry/canonical-bundle-complex-manifold"
title = "Canonical bundle of a complex manifold"
kind = "definition"
summary = "The holomorphic line bundle of holomorphic differential forms of top degree on a complex manifold."
aliases = ["holomorphic canonical bundle", "bundle of holomorphic top forms"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/holomorphic-cotangent-bundle", "differential-geometry/holomorphic-line-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]] of complex dimension \(n\). Its **canonical bundle** is the top exterior power
\[
K_X=\bigwedge\nolimits^n T^{*1,0}X=\Omega_X^n
\]
of the [[differential-geometry/holomorphic-cotangent-bundle|holomorphic cotangent bundle]]. It is a [[differential-geometry/holomorphic-line-bundle|holomorphic line bundle]] whose fiber at \(x\) consists of alternating complex \(n\)-linear forms on \(T_x^{1,0}X\). In holomorphic coordinates \(z^1,\ldots,z^n\), the form \(dz^1\wedge\cdots\wedge dz^n\) is a local holomorphic frame. Thus local sections are holomorphic top-degree forms, and the bundle is determined without choosing a metric or orientation.

## Coordinate transformations

Under a holomorphic coordinate change \(w=w(z)\), the standard local frames satisfy
\[
dw^1\wedge\cdots\wedge dw^n
=\det\left(\frac{\partial w}{\partial z}\right)
dz^1\wedge\cdots\wedge dz^n.
\]
The [[real-analysis/jacobian-determinant|Jacobian determinant]] is nowhere zero on a coordinate overlap, so these factors are precisely the [[fiber-bundles/transition-function|transition functions]] of \(K_X\). This also explains why top forms, rather than their coefficient functions alone, are coordinate-independent objects.

## Sections and triviality

A [[differential-geometry/holomorphic-section|holomorphic section]] of \(K_X\) is a holomorphic \(n\)-form. A nowhere-vanishing global holomorphic \(n\)-form determines an isomorphism \(K_X\cong X\times\mathbb C\); conversely, any holomorphic trivialization supplies such a form. The form is additional data, however: triviality asserts existence and does not choose a preferred trivializing section.

## Examples and scope

On \(\mathbb C^n\), the form \(dz^1\wedge\cdots\wedge dz^n\) trivializes the canonical bundle. For the Riemann sphere, the coordinate change \(w=1/z\) gives \(dw=-z^{-2}dz\); its canonical bundle is therefore nontrivial and has degree \(-2\).

**Warning.** This analytic canonical bundle should not be conflated with a canonical module of a singular ring or scheme. On a smooth complex algebraic variety, analytification of the algebraic canonical [[fiber-bundles/line-bundle|line bundle]] gives the bundle defined here.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §2.2, holomorphic cotangent bundles, exterior powers, and the canonical bundle.
2. Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry*, Wiley, 1978. [DOI record](https://doi.org/10.1002/9781118032527). Relevant: Chapter 0, holomorphic vector bundles and differential forms.
