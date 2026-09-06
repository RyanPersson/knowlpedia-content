+++
id = "langlands/intersection-cohomology-complex"
title = "Intersection-cohomology complex"
kind = "definition"
summary = "The perverse middle extension of a shifted local system from a smooth dense stratum."
aliases = ["IC complex", "intersection-cohomology sheaf"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["fiber-bundles/local-system", "langlands/perverse-sheaf"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be an irreducible complex algebraic variety of dimension \(d\), let
\(j:U\hookrightarrow X\) be a smooth dense open subset, and let
\(\mathcal L\) be a [[fiber-bundles/local-system|local system]] on \(U\). The **intersection-cohomology
complex** is the [[langlands/perverse-sheaf|perverse middle extension]]
\[
\operatorname{IC}_X(\mathcal L)=j_{!*}\bigl(\mathcal L[d]\bigr).
\]

It is characterized as the extension having no nonzero perverse subobject or
quotient supported on \(X\setminus U\). For the constant local system, its
hypercohomology is the intersection cohomology of \(X\).

## References

1. Alexander Beilinson, Joseph Bernstein, and Pierre Deligne, *Faisceaux
   pervers*, Astérisque 100, Société Mathématique de France, 1982.
