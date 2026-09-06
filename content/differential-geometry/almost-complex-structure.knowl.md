+++
id = "differential-geometry/almost-complex-structure"
title = "Almost-complex structure"
kind = "definition"
summary = "A smooth tangent-bundle endomorphism whose square is minus the identity."
aliases = ["almost complex structure"]
domains = ["differential-geometry", "fiber-bundles"]
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/tangent-space", "fiber-bundles/vector-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **almost-complex structure** on a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\) is a smooth vector-bundle endomorphism
\[
J:TM\to TM
\]
such that
\[
J^2=-\operatorname{id}_{TM}.
\]
Thus each real [[differential-geometry/tangent-space|tangent space]] becomes a complex vector space by declaring multiplication by \(i\) to be \(J\). In particular, \(M\) must have even real dimension. This is pointwise linear-algebraic data varying smoothly; no coordinate integrability is included.

Every [[differential-geometry/complex-manifold|complex manifold]] has a canonical almost-complex structure. An arbitrary almost-complex structure need not come from [[differential-geometry/complex-coordinate-chart|complex coordinate charts]]; when it does, it is [[differential-geometry/integrable-almost-complex-structure|integrable]].

Maps preserving this structure are the
[[differential-geometry/almost-complex-map|almost-complex, \(J\)-holomorphic,
or pseudoholomorphic maps]]. Their tangent maps intertwine the two
almost-complex structures.

## Examples and constraints

The standard multiplication-by-\(i\) map on \(\mathbb C^n\cong\mathbb R^{2n}\) is an almost-complex structure. A [[differential-geometry/symplectic-manifold|symplectic manifold]] admits compatible almost-complex structures, although none is selected by the symplectic form alone. By contrast, an odd-dimensional manifold cannot carry an almost-complex structure because a real vector space with an endomorphism squaring to \(-1\) has even dimension.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Chapter 1, complex and almost-complex structures.
2. Dusa McDuff and Dietmar Salamon, *J-Holomorphic Curves and Symplectic Topology*, 2nd ed., AMS, 2012. [DOI record](https://doi.org/10.1090/coll/052). Relevant: Chapter 2, almost-complex structures and \(J\)-holomorphic maps.
