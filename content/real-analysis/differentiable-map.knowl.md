+++
id = "real-analysis/differentiable-map"
title = "Differentiable map"
kind = "knowl"
summary = "A map between Euclidean spaces is differentiable at a point when it has a first-order linear approximation there."
aliases = ["differentiable-map", "Differentiable map"]
domains = ["real-analysis"]
prerequisites = ["linear-algebra/euclidean-norm", "real-analysis/frechet-derivative"]
dependency_review_count = 1
legacy_source_path = "real-analysis/differentiable-map.md"
+++

Let \(U\subseteq\mathbb R^n\) be open, let \(a\in U\), and let \(f:U\to\mathbb R^m\). The map \(f\) is **differentiable at \(a\)** if there is a linear map \(L:\mathbb R^n\to\mathbb R^m\) such that
\[
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-Lh\|}{\|h\|}=0,
\]

where \(h\) is small enough that \(a+h\in U\), and \(\|\cdot\|\) is the [[linear-algebra/euclidean-norm|Euclidean norm]].

The map \(L\), which is necessarily unique, is the [[real-analysis/frechet-derivative|Fréchet derivative]] \(Df(a)\). In standard coordinates it is represented by the [[real-analysis/jacobian-matrix|Jacobian matrix]].

## Examples

- Any affine map \(f(x)=Ax+b\) is differentiable everywhere, with derivative \(Df(x)h=Ah\).
- The map \(f:\mathbb{R}^2\to \mathbb{R}^3\) given by \(f(x,y)=(x^2,xy,\sin y)\) is differentiable everywhere.
