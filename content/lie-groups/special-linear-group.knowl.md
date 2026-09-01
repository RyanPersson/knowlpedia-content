+++
id = "lie-groups/special-linear-group"
title = "Special linear group"
kind = "knowl"
summary = "The determinant-one matrix group, with dimensions distinguished over the real and complex numbers."
aliases = ["special-linear-group", "Special linear group"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/general-linear-group", "lie-groups/lie-subgroup", "lie-groups/closed-subgroup-lie-group", "lie-groups/underlying-real-lie-group", "lie-groups/special-linear-lie-algebra", "lie-groups/exponential-map-lie-group", "lie-groups/semisimple-lie-algebra", "lie-groups/root-system"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "lie-groups/special-linear-group.md"
+++

For a field \(\mathbb F\) equal to \(\mathbb R\) or \(\mathbb C\), the **special linear group** is
\[
SL(n,\mathbb F)=\{A\in GL(n,\mathbb F): \det(A)=1\},
\]
viewed as a matrix Lie group inside the [[lie-groups/general-linear-group|general linear group]]. It is a closed Lie subgroup (see [[lie-groups/lie-subgroup|Lie subgroup]] and [[lie-groups/closed-subgroup-lie-group|closed subgroup]]), hence a Lie group in its own right.

The dimension depends on the scalar field:
\[
\dim_{\mathbb R}SL(n,\mathbb R)=n^2-1,\qquad
\dim_{\mathbb C}SL(n,\mathbb C)=n^2-1.
\]
Consequently, the [[lie-groups/underlying-real-lie-group|underlying real Lie group]] \(SL(n,\mathbb C)_{\mathbb R}\) has real dimension \(2(n^2-1)\). An unqualified statement that \(SL(n,\mathbb C)\) has manifold dimension \(n^2-1\) is correct only when “dimension” means complex dimension.

Its Lie algebra is the trace-zero matrices,
the [[lie-groups/special-linear-lie-algebra|special linear Lie algebra]] \(\mathfrak{sl}_n(\mathbb F)\), and the exponential map restricts to \(\exp:\mathfrak{sl}_n(\mathbb F)\to SL(n,\mathbb F)\) (see [[lie-groups/exponential-map-lie-group|exponential map]]). The determinant condition differentiates to the trace condition:
\[
\left.\frac{d}{dt}\right|_{t=0}\det(I+tX)=\mathrm{tr}(X).
\]

The groups \(SL(n,\mathbb R)\) and \(SL(n,\mathbb C)\) are basic examples of connected linear Lie groups, and they play a central role in semisimple theory (compare [[lie-groups/semisimple-lie-algebra|semisimple Lie algebras]] and the root-theoretic framework starting at [[lie-groups/root-system|root systems]]).

## References

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, §§2.1–2.2. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter I. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
