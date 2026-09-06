+++
id = "differential-geometry/critical-value-of-a-smooth-map"
title = "Critical value of a smooth map"
kind = "definition"
summary = "A target point whose fiber contains a critical point of the smooth map."
aliases = ["singular value of a smooth map", "critical value on a manifold"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-map", "differential-geometry/critical-point-of-a-smooth-map", "fiber-bundles/regular-value"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(f:M\to N\) be a [[fiber-bundles/smooth-map|smooth map]]. A point \(y\in N\) is a **critical value of \(f\)** if there exists \(p\in f^{-1}(y)\) that is a [[differential-geometry/critical-point-of-a-smooth-map|critical point of \(f\)]]. Equivalently, \(y\) is critical when at least one differential
\[
df_p:T_pM\longrightarrow T_yN,\qquad p\in f^{-1}(y),
\]
fails to be surjective. Thus the critical values form the image under \(f\) of the critical-point set. A [[fiber-bundles/regular-value|regular value]] instead requires surjectivity at every point of its fiber, so critical and regular values are complementary subsets of \(N\).

## Empty fibers

If \(y\notin f(M)\), then \(f^{-1}(y)\) is empty. The universal condition in the definition of a regular value is therefore vacuously satisfied, whereas the existential condition for a critical value fails. Consequently, every point outside the image of \(f\) is regular and is not critical.

## Examples

For \(f:\mathbb R\to\mathbb R\), \(f(x)=x^2\), the only critical point is \(0\), so the only critical value is \(0\). For the height function on the unit sphere, the north and south poles are critical points and their heights \(1\) and \(-1\) are critical values. Distinct critical points may have the same critical value.

## Sard's theorem

[[differential-geometry/sards-theorem|Sard's theorem]] says that the set of critical values of a smooth map between finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] has measure zero in the target, in the coordinate-invariant sense. It may nevertheless be topologically complicated or dense for maps of lower differentiability.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: regular and critical values and Sard's theorem.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 1, regular values and Sard's theorem.
