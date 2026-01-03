---
title: "Schwarz's Theorem (Clairaut's theorem)"
description: "Under continuity of second partials, mixed partial derivatives are equal"
---

**Schwarz (Clairaut) Theorem**: Let $U\subseteq\mathbb{R}^n$ be open and let $f:U\to\mathbb{R}$. Fix indices $i\neq j$. If the {{< knowl id="mixed-partial-derivative" text="mixed second partial derivatives" >}} $\frac{\partial^2 f}{\partial x_i\partial x_j}$ and $\frac{\partial^2 f}{\partial x_j\partial x_i}$ exist on a {{< knowl id="neighborhood" text="neighborhood" >}} of $a\in U$ and are {{< knowl id="continuity-at-a-point" text="continuous" >}} at $a$, then
$
\frac{\partial^2 f}{\partial x_i\partial x_j}(a)=\frac{\partial^2 f}{\partial x_j\partial x_i}(a).
$

This theorem ensures symmetry of the {{< knowl id="hessian-matrix" text="Hessian matrix" >}} under standard smoothness hypotheses and is used throughout multivariable analysis and optimization.
