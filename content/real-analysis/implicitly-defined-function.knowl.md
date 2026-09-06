+++
id = "real-analysis/implicitly-defined-function"
title = "Implicitly defined function"
kind = "knowl"
summary = "A function specified indirectly by an equation involving its inputs and outputs"
aliases = ["implicitly-defined-function", "Implicitly defined function"]
domains = ["real-analysis"]
prerequisites = ["shared-foundations/function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/implicitly-defined-function.md"
+++

Let \(F\) be a function on a subset of \(\mathbb R^{n+m}\). A function \(\varphi:U\to\mathbb R^m\), where \(U\subseteq\mathbb R^n\), is **implicitly defined by**
\[
F(x,y)=0
\]
on \(U\) if \(F(x,\varphi(x))=0\) for every \(x\in U\).

## Remarks

An equation need not determine \(y\) uniquely or even determine it at all. The [[real-analysis/implicit-function-theorem|implicit function theorem]] gives local existence and uniqueness near a solution \((x_0,y_0)\) when \(F\) is continuously differentiable and the derivative with respect to \(y\) is invertible there.

## Examples

- The equation \(x^2+y^2-1=0\) implicitly defines \(y=\sqrt{1-x^2}\) near \((0,1)\), and \(y=-\sqrt{1-x^2}\) near \((0,-1)\).
- The equation \(x+y+z=0\) implicitly defines \(z=-(x+y)\) as a function of \((x,y)\) on all of \(\mathbb R^2\).
