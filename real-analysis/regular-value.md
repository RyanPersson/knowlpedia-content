---
title: "Regular value"
description: "A value whose entire preimage consists of regular points"
---

A **regular value** of a differentiable map $F:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$ and $m\le n$) is a point $y\in \mathbb{R}^m$ such that every $a\in F^{-1}(\{y\})$ is a {{< knowl id="regular-point" text="regular point" >}} of $F$.

Regular values are the “good” level values for which the constraint set $F^{-1}(\{y\})$ behaves well locally, which is why they appear naturally in the {{< knowl id="implicit-function-theorem" text="implicit function theorem" >}} and in constrained optimization on a {{< knowl id="constraint-set" text="constraint set" >}}.

**Examples:**
- For $F(x,y)=x^2+y^2$, the value $1$ is a regular value, since on the level set $x^2+y^2=1$ the gradient is never zero.
- For $F(x,y,z)=x+y+z$, every value $y\in\mathbb{R}$ is a regular value, since the derivative is surjective at every point.
