+++
id = "real-analysis/frechet-derivative"
title = "Fréchet derivative"
kind = "knowl"
summary = "The derivative of a multivariable function as a best linear approximation at a point"
aliases = ["frechet-derivative", "Fréchet derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/frechet-derivative.md"
prerequisites = ["shared-foundations/function", "linear-algebra/normed-vector-space", "functional-analysis/bounded-linear-operator", "topology/open-set", "real-analysis/limit-of-a-function-at-a-point"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++


Let \(E,F\) be real [[linear-algebra/normed-vector-space|normed vector spaces]], \(U\subset E\) open, and \(a\in U\). The **Fréchet derivative** of \(f:U\to F\) at \(a\) is a [[functional-analysis/bounded-linear-operator|bounded linear map]] \(Df(a):E\to F\) such that
\[
\lim_{h\to0,\ h\ne0}\frac{\|f(a+h)-f(a)-Df(a)h\|_F}{\|h\|_E}=0.
\]
It is the linear approximation with an error negligible compared with the size of the increment. Completeness of the spaces is not required.

## Uniqueness

If \(L_1,L_2\) both satisfy the definition, use increments \(h=tv\) for a fixed vector \(v\). Dividing the difference of their remainders by \(|t|\) and letting \(t\to0\) gives \((L_1-L_2)v=0\). Thus the derivative is unique.

## Euclidean spaces

For \(E=\mathbb R^n,F=\mathbb R^m\), the derivative is represented by the [[real-analysis/jacobian-matrix|Jacobian matrix]]. Fréchet differentiability implies existence of the partial derivatives; their existence alone does not imply Fréchet differentiability. For \(f(x,y)=(x^2y,x+y)\),
\[
Df(a,b)=\begin{pmatrix}2ab&a^2\\1&1\end{pmatrix}.
\]
A bounded linear function \(f(x)=Ax\) has derivative \(Df(a)=A\) at every point.
