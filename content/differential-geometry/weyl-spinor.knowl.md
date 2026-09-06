+++
id = "differential-geometry/weyl-spinor"
title = "Weyl spinor"
kind = "definition"
summary = "A complex spinor lying in one of the two half-spin representations in even dimension."
aliases = ["chiral spinor", "half-spinor"]
domains = ["differential-geometry", "mathematical-physics"]
prerequisites = ["linear-algebra/quadratic-form", "differential-geometry/spinor-module", "differential-geometry/chirality-operator", "differential-geometry/clifford-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be an even-dimensional oriented [[linear-algebra/quadratic-form|quadratic space]] and let
\[
\Delta=\Delta^+\oplus\Delta^-
\]
be a complex [[differential-geometry/spinor-module|spinor module]] decomposed
into the \(+1\) and \(-1\) eigenspaces of its
[[differential-geometry/chirality-operator|chirality operator]]. A **Weyl
spinor** of positive or negative chirality is an element of \(\Delta^+\) or
\(\Delta^-\), respectively.

On an even-dimensional spin manifold, a Weyl spinor field is a section of one
of the half-spinor bundles \(S^+\) or \(S^-\). [[differential-geometry/clifford-module|Clifford multiplication]] by a
vector reverses chirality:
\[
c(v):\Delta^\pm\longrightarrow\Delta^\mp.
\]

The definition requires even dimension and a complex chiral spin
representation. A compatible reality condition is separate data; when one
exists and preserves a half-spin representation, it defines
[[differential-geometry/majorana-weyl-spinor|Majorana–Weyl spinors]].

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I, §5.
2. Pierre Deligne, “Notes on spinors,” in *Quantum Fields and Strings: A
   Course for Mathematicians*, Volume 1, American Mathematical Society, 1999,
   pp. 99–135.
