+++
id = "real-analysis/frechet-derivative"
title = "Fréchet derivative"
kind = "knowl"
summary = "The derivative of a multivariable function as a best linear approximation at a point"
aliases = ["frechet-derivative", "Fréchet derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/frechet-derivative.md"
prerequisites = ["shared-foundations/function", "linear-algebra/linear-map", "linear-algebra/euclidean-norm"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **Fréchet derivative** of a [[shared-foundations/function|function]] \(f:U\to \mathbb{R}^m\) (with \(U\subseteq \mathbb{R}^n\) open) at a point \(a\in U\) is a [[linear-algebra/linear-map|linear map]] \(Df(a):\mathbb{R}^n\to \mathbb{R}^m\) such that
\[
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-Df(a)h\|}{\|h\|}=0,
\]

where \(\|\cdot\|\) is the [[linear-algebra/euclidean-norm|Euclidean norm]].

## Uniqueness and differentiability

If such a map exists, it is unique; it is the linear part of the first-order approximation \(f(a+h)=f(a)+Df(a)h+o(\|h\|)\). If \(f\) is Fréchet differentiable at \(a\), its partial derivatives exist and \(Df(a)\) is represented by the [[real-analysis/jacobian-matrix|Jacobian matrix]] at \(a\). Existence of \(Df(a)\) is the defining condition for a [[real-analysis/differentiable-map|differentiable map]] at \(a\); existence of partial derivatives alone does not suffice.

## Examples

- If \(f(x)=Ax\) for a fixed matrix \(A\), then \(Df(a)h=Ah\) for every \(a\).
- For \(f:\mathbb{R}^2\to \mathbb{R}^2\) given by \(f(x,y)=(x^2y,\,x+y)\), the derivative at \((a,b)\) is the linear map represented by the matrix
\[
  \begin{pmatrix}
  2ab & a^2\\
  1 & 1
  \end{pmatrix}.
\]
