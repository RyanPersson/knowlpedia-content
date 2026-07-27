+++
id = "real-analysis/regular-point"
title = "Regular point"
kind = "knowl"
summary = "A point where a differentiable map has maximal rank or a surjective derivative"
aliases = ["regular-point", "Regular point"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/regular-point.md"
+++

A **regular point** of a differentiable map \(F:U\to \mathbb{R}^m\), where \(U\subseteq\mathbb R^n\) is open, is a point \(a\in U\) such that the [[real-analysis/frechet-derivative|Fréchet derivative]] \(DF(a):\mathbb{R}^n\to \mathbb{R}^m\) is surjective.

## Equivalent characterizations

Equivalently, the [[real-analysis/jacobian-matrix|Jacobian matrix]] \(JF(a)\) has rank \(m\). Thus regular points can exist only when \(m\le n\).

## Remarks

Regular points are the local nondegeneracy condition used in the [[real-analysis/implicit-function-theorem|implicit function theorem]] and in the definition of a [[fiber-bundles/regular-value|regular value]].

## Examples

- For \(F(x,y)=x^2+y^2\), every point \((x,y)\ne(0,0)\) is regular because the gradient \((2x,2y)\) is nonzero.
- For \(F(x,y)=(x^2,y^2)\), the point \((1,1)\) is regular, while \((0,1)\) is not because the Jacobian has rank \(1\) there.
