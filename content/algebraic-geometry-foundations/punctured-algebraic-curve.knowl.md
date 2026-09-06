+++
id = "algebraic-geometry-foundations/punctured-algebraic-curve"
title = "Punctured algebraic curve"
kind = "definition"
summary = "The complement of a finite reduced divisor in an algebraic curve."
aliases = ["punctured curve"]
domains = ["algebraic-geometry-foundations", "langlands"]
prerequisites = ["algebraic-geometry-foundations/algebraic-curve", "algebraic-geometry-foundations/pointed-algebraic-curve"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be an
[[algebraic-geometry-foundations/algebraic-curve|algebraic curve]] over a
field \(k\), and let \(D\subset X\) be a finite reduced closed subscheme. The
open subscheme
\[
U=X\setminus D
\]
is the **punctured algebraic curve** obtained by removing \(D\).

If \(X\) is smooth and \(D=\{x_1,\ldots,x_n\}\) consists of distinct marked
points, then the
[[algebraic-geometry-foundations/pointed-algebraic-curve|pointed curve]]
\((X;x_1,\ldots,x_n)\) determines \(U\). The pointed curve retains the marked
sections and their labels, while \(U\) generally does not.

## Langlands role

Ramified [[fiber-bundles/local-system|local systems]] live on \(U\) together with conditions describing
their behavior around the missing divisor \(D\). Those boundary conditions
are extra data, not part of the definition of the punctured curve.

## References

1. Pierre Deligne, *Équations différentielles à points singuliers réguliers*,
   Lecture Notes in Mathematics 163, Springer, 1970.
   [DOI](https://doi.org/10.1007/BFb0061194).
