+++
id = "differential-geometry/nijenhuis-tensor"
title = "Nijenhuis tensor of an almost-complex structure"
kind = "definition"
summary = "The tensor measuring the failure of an almost-complex structure to be integrable."
aliases = ["Nijenhuis tensor"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/almost-complex-structure", "fiber-bundles/lie-bracket", "fiber-bundles/tangent-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(J\) be an
[[differential-geometry/almost-complex-structure|almost-complex structure]]
on a smooth manifold \(M\). Its **Nijenhuis tensor** is the vector-valued
two-form
\[
N_J(X,Y)
=[JX,JY]-J[JX,Y]-J[X,JY]-[X,Y]
\]
for smooth vector fields \(X,Y\).

Although the formula uses [[fiber-bundles/lie-bracket|Lie brackets]], its value at a point depends only on
the values of \(X\) and \(Y\) there, so
\(N_J\in\Omega^2(M;TM)\). After complexifying the [[fiber-bundles/tangent-bundle|tangent bundle]], \(N_J=0\)
exactly when the \(+i\)-eigenbundle of \(J\) is closed under Lie brackets.

The [[differential-geometry/newlander-nirenberg-theorem|Newlander–Nirenberg
theorem]] identifies the vanishing of \(N_J\) with integrability in the
smooth category.

## References
Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005.
[DOI record](https://doi.org/10.1007/b137952). Relevant: Chapter 1.
