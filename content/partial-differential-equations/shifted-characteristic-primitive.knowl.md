+++
id = "partial-differential-equations/shifted-characteristic-primitive"
title = "Shifted characteristic primitive on a torus"
kind = "definition"
summary = "An integral along a constant torus drift inverts a transport derivative."
aliases = ["fixed-shift transport integral"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/transport-equation", "real-analysis/directional-derivative", "topology/flat-torus", "measure-theory/differentiation-under-integral", "real-analysis/fundamental-theorem-of-calculus-i", "functional-analysis/test-function-space", "measure-theory/lebesgue-integral"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(F(s,y)\) be smooth on \(\mathbb R\times\mathbb T^n\) with support in a fixed bounded interval in \(s\). For fixed \(M\in\mathbb R\) and \(v\in\mathbb R^n\), define
\[
I^-F(U,y)=\int_{-\infty}^U F(s,y+M(s-U)v)\,ds,
\qquad
I^+F(U,y)=\int_U^\infty F(s,y+M(s-U)v)\,ds.
\]
These are **characteristic primitives** for the [[partial-differential-equations/transport-equation|transport derivative]] \(D_M=\partial_U+M v\cdot\nabla_y\). They satisfy \(D_MI^-F=F\) and \(D_MI^+F=-F\).

## Fixed-shift representation

With \(s=U+z\), the two integration intervals become \(( -\infty,0)\) and \((0,\infty)\), and the integrand is \(F(U+z,y+Mzv)\). Differentiating in \(U,y\), or any additional smooth parameter on which only \(F\) depends, now differentiates the source without a factor of \(M\). If the source interval has length \(L\), each such derivative is bounded by \(L\) times the corresponding source supremum. The parameters \(M,v\) are held fixed in these estimates.

The sum \(JF=I^-F+I^+F\) solves \(D_MJF=0\). It generally does not have compact support in \(U\), even though \(F\) does.
