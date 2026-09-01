+++
id = "langlands/affine-schubert-variety"
title = "Affine Schubert variety"
kind = "definition"
summary = "The closure of a positive-loop-group orbit in the affine Grassmannian."
aliases = ["Schubert variety in the affine Grassmannian"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands/dominant-coweight", "langlands/positive-loop-group", "langlands/affine-grassmannian"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a split connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over an algebraically closed
field, choose a split maximal torus, and let \(\lambda\) be a
[[langlands/dominant-coweight|dominant coweight]]. The [[langlands/positive-loop-group|positive loop group]]
\(L^+G\) acts on the [[langlands/affine-grassmannian|affine Grassmannian]],
and the orbit through \(t^\lambda\) is the affine Schubert cell
\(\operatorname{Gr}_G^\lambda\).

The **affine Schubert variety**
\[
\operatorname{Gr}_G^{\leq\lambda}
=\overline{\operatorname{Gr}_G^\lambda}
\]
is its reduced closure. It is a finite-dimensional projective variety, and
its boundary is the union of cells indexed by dominant coweights below
\(\lambda\) in the dominance order.

## References

1. Ivan Mirković and Kari Vilonen, “Geometric Langlands duality and
   representations of algebraic groups over commutative rings,” *Annals of
   Mathematics* 166 (2007), 95–143.
   [arXiv](https://arxiv.org/abs/math/0401222).
