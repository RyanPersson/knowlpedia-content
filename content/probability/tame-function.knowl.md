+++
id = "probability/tame-function"
title = "Tame Function (Segal)"
kind = "knowl"
summary = "A function on an infinite-dimensional Hilbert space depending on finitely many coordinates"
aliases = ["tame-function", "Tame Function (Segal)"]
domains = ["probability"]
legacy_source_path = "shale-paper/tame-function.md"
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/orthogonal-projection"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 2
+++

A function \(f\) on a real [[linear-algebra/hilbert-space|Hilbert space]] \(M\) is **tame** if
\(f(x)=\bar f(Px)\) for some finite-dimensional subspace \(M'\) and [[linear-algebra/orthogonal-projection|projection]] \(P:M\to M'\).

## Remarks

**Key properties (paper use):**
- Tame functions generate the σ-algebra \(\mathfrak R\) of the Gaussian [[probability/probability-space|probability space]].
- Integrals are defined first on tame functions via finite-dimensional Gaussian integrals.

## Examples

- \(f(x)=\exp(i(x,e))\) depends only on the 1D coordinate \((x,e)\).
