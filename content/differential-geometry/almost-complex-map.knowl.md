+++
id = "differential-geometry/almost-complex-map"
title = "Almost-complex map"
kind = "definition"
summary = "A smooth map whose tangent map intertwines the almost-complex structures."
aliases = ["J-holomorphic map", "pseudoholomorphic map"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-map", "differential-geometry/almost-complex-structure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((M,J_M)\) and \((N,J_N)\) be smooth manifolds with
[[differential-geometry/almost-complex-structure|almost-complex
structures]]. A smooth map \(f:M\to N\) is an **almost-complex map**, also
called a **\(J\)-holomorphic map** or **pseudoholomorphic map**, if
\[
df\circ J_M=J_N\circ df.
\]
Equivalently, every tangent map
\(df_p:T_pM\to T_{f(p)}N\) is complex-linear for the complex structures
defined by \(J_M\) and \(J_N\).

Identity maps, constant maps, and composites of almost-complex maps are
almost-complex. If an almost-complex map is a diffeomorphism, its inverse is
also almost-complex. Thus almost-complex manifolds and almost-complex maps
form a category.

When both structures are
[[differential-geometry/integrable-almost-complex-structure|integrable]], the
intertwining equation is equivalent to \(f\) being a
[[differential-geometry/holomorphic-map|holomorphic map]]. For nonintegrable
structures it remains meaningful, notably for pseudoholomorphic curves in
symplectic geometry.

## References
Dusa McDuff and Dietmar Salamon, *J-Holomorphic Curves and Symplectic
Topology*, 2nd ed., AMS, 2012.
[DOI record](https://doi.org/10.1090/coll/052). Relevant: Chapter 2.
