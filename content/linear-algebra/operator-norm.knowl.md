+++
id = "linear-algebra/operator-norm"
title = "Operator norm"
kind = "knowl"
summary = "Norm of a linear map defined by its maximal expansion of unit vectors."
aliases = ["operator-norm", "Operator norm"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/operator-norm.md"
prerequisites = ["linear-algebra/linear-map", "linear-algebra/normed-vector-space", "real-analysis/supremum"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

An **operator norm** of a [[linear-algebra/linear-map|linear map]] \(T:V\to W\) between [[linear-algebra/normed-vector-space|normed vector spaces]] \((V,\|\cdot\|_V)\) and \((W,\|\cdot\|_W)\) is the quantity
\[
\|T\|=\sup_{\|v\|_V\le 1}\|T(v)\|_W,
\]
with the understanding that the supremum may be \(+\infty\) in general. When \(\|T\|<\infty\), one says \(T\) is bounded.

## Equivalent formulas

For \(V\ne\{0\}\), this also equals
\[
\sup_{v\ne0}\frac{\|T(v)\|_W}{\|v\|_V}=\sup_{\|v\|_V=1}\|T(v)\|_W.
\]
For the zero vector space, the unit-ball formula gives \(\|T\|=0\).

## Remarks

For linear maps between normed spaces, finiteness of the operator norm is equivalent to being [[topology/continuous-map|continuous]]. The operator norm makes the collection of bounded linear maps into a normed vector space and specializes to a norm on [[linear-algebra/linear-operator|linear operators]] when \(V=W\).

## Examples

- If \(T(v)=c\,v\) on a normed space, then \(\|T\|=|c|\).
- For the projection \(P(x,y)=(x,0)\) on \(\mathbb{R}^2\) with the Euclidean norm, \(\|P\|=1\).
- For a diagonal matrix \(A=\operatorname{diag}(d_1,\dots,d_n)\) acting on \(\mathbb{R}^n\) with the max norm, the induced operator norm is \(\|A\|=\max_i |d_i|\).
