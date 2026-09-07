+++
id = "real-analysis/class-ck-map"
title = "Class C^k map"
kind = "knowl"
summary = "A map with continuous partial derivatives up to order k."
aliases = ["class-ck-map", "Class C^k map"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/class-ck-map.md"
prerequisites = ["shared-foundations/function", "real-analysis/partial-derivative", "topology/open-set", "topology/continuous-map"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

For a nonnegative integer \(k\), a **class \(C^k\) map** is a [[shared-foundations/function|function]] \(F:U\to\mathbb{R}^m\) defined on an open set \(U\subseteq\mathbb{R}^n\) such that all partial derivatives of \(F\) of total order at most \(k\) exist on \(U\) and are continuous on \(U\) (with order \(0\) meaning \(F\) itself).

A map is **class \(C^\infty\)**, or **smooth**, if it is class \(C^k\) for every nonnegative integer \(k\).

## Derivative descriptions

When \(k=1\), this is the standard “continuously differentiable” hypothesis in multivariable calculus: the derivative is encoded by the [[real-analysis/jacobian-matrix|Jacobian matrix]], and \(C^1\) regularity is closely aligned with having a continuous [[real-analysis/frechet-derivative|Fréchet derivative]]. Higher regularity interacts with mixed derivatives via results like the [[real-analysis/schwarz-clairaut-theorem|Schwarz–Clairaut theorem]].

## Examples

- The map \(F(x,y)=(x^2+y,\;xy)\) is class \(C^\infty\) on \(\mathbb{R}^2\).
- The map \(F(x,y)=(|x|,\;y)\) is class \(C^0\) on \(\mathbb{R}^2\) but not class \(C^1\) along the line \(x=0\).
