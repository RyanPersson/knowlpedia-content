+++
id = "real-analysis/partial-derivative"
title = "Partial derivative"
kind = "knowl"
summary = "Derivative of a multivariable function with respect to one coordinate"
aliases = ["partial-derivative", "Partial derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/partial-derivative.md"
prerequisites = ["real-analysis/differentiable-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(U\subseteq\mathbb R^n\) be open, \(f:U\to\mathbb R^m\), and \(a\in U\). The **partial derivative of \(f\) at \(a\) with respect to the \(j\)-th coordinate** is
\[
\frac{\partial f}{\partial x_j}(a)
=\lim_{t\to0}\frac{f(a+t e_j)-f(a)}{t},
\]
when this limit exists in \(\mathbb R^m\).

Partial derivatives are the entries of the [[real-analysis/jacobian-matrix|Jacobian matrix]]. Existence of every partial derivative at \(a\) does not by itself imply that \(f\) is [[real-analysis/differentiable-map|differentiable]] at \(a\).

## Examples

- For \(f(x,y)=x^2y\), one has \(\frac{\partial f}{\partial x}=2xy\) and \(\frac{\partial f}{\partial y}=x^2\).
- For \(f(x,y)=|x|\), the partial derivative \(\frac{\partial f}{\partial x}(0,y)\) does not exist.
