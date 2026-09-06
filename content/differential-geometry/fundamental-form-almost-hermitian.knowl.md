+++
id = "differential-geometry/fundamental-form-almost-hermitian"
title = "Fundamental 2-form of an almost-Hermitian manifold"
kind = "definition"
summary = "The nondegenerate real 2-form obtained by pairing an almost-complex structure with its compatible metric."
aliases = ["associated 2-form", "fundamental form"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/almost-hermitian-manifold", "fiber-bundles/tangent-space-at-a-point", "fiber-bundles/differential-k-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((M,J,g)\) be an [[differential-geometry/almost-hermitian-manifold|almost-Hermitian manifold]]. Its **fundamental \(2\)-form** is the differential form \(\omega\) defined by
\[
\omega(X,Y)=g(JX,Y)
\]
for [[fiber-bundles/tangent-space-at-a-point|tangent vectors]] \(X,Y\) at the same point. Compatibility of \(g\) with \(J\) makes \(\omega\) skew-symmetric, while positivity of \(g\) makes it nondegenerate. Thus \(\omega\) is a smooth, nondegenerate real [[fiber-bundles/differential-k-form|\(2\)-form]], but it need not be closed. The displayed order fixes the sign convention: interchanging \(X\) and \(JY\) changes the sign.

## Recovering the compatible data

The form and [[differential-geometry/almost-complex-structure|almost-complex structure]] recover the metric by
\[
g(X,Y)=\omega(X,JY).
\]
Conversely, compatible pairs among \(J\), \(g\), and \(\omega\), together with the appropriate positivity condition, determine the third object. This is pointwise Hermitian linear algebra applied smoothly to the [[fiber-bundles/tangent-bundle|tangent bundle]].

## Closedness and integrability

If \(d\omega=0\), the almost-Hermitian structure is called almost Kähler, and \(\omega\) is a symplectic form. If \(J\) is [[differential-geometry/integrable-almost-complex-structure|integrable]], the structure is Hermitian. It is Kähler when both conditions hold. Neither [[fiber-bundles/closed-differential-form|closedness]] of \(\omega\) nor integrability of \(J\) follows from compatibility alone.

## Conventions and scope

**Warning.** Many authors instead define the fundamental form by \(\omega(X,Y)=g(X,JY)\), which is the negative of the convention here. Either convention is valid, but formulas involving \(d^c\), curvature, and Hamiltonian signs must be adjusted consistently.

## References

1. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. II, Wiley, 1969. [Publisher record](https://www.wiley.com/en-us/Foundations+of+Differential+Geometry%2C+Volume+2-p-9780471157328). Relevant: Chapter IX, §1, almost-Hermitian structures and their fundamental forms.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Chapter 3, Hermitian and Kähler geometry.
