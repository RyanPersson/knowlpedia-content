+++
id = "algebra-fields-galois/completion-at-place"
title = "Completion of a field at a place"
kind = "definition"
summary = "The complete topological field obtained from a field and one of its places."
aliases = ["completion at a place", "local completion", "completion of a global field"]
domains = ["algebra-fields-galois", "topology", "langlands"]
prerequisites = ["algebra-fields-galois/place-of-global-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a field with an absolute value \(|\cdot|_v\) representing a
[[algebra-fields-galois/place-of-global-field|place]] \(v\). The
**completion of \(F\) at \(v\)** is a complete valued field \(F_v\) together
with an isometric embedding
\[
F\longrightarrow F_v
\]
having dense image. It is unique up to a unique isometric isomorphism fixing
\(F\).

## Construction

The field \(F_v\) is obtained by taking equivalence classes of Cauchy
sequences for the metric \(d_v(x,y)=|x-y|_v\). Addition, multiplication, and
the absolute value extend continuously from \(F\).

## Global-field cases

If \(F\) is a [[langlands-letter/knowls/global-local-fields-completions|global field]], every \(F_v\) is a [[algebra-fields-galois/local-field|local field]].
For a number field, an archimedean completion is \(\mathbb R\) or
\(\mathbb C\), while a nonarchimedean completion is a finite extension of
\(\mathbb Q_p\). For a global function field, it is a finite extension of a
Laurent-series field over a finite field.

## References

1. Jürgen Neukirch, *Algebraic Number Theory*, Springer, 1999, Chapter II,
   §§4--5.
2. Jean-Pierre Serre, *Local Fields*, Springer, 1979, Chapter I.
