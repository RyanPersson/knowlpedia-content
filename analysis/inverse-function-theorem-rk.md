---
title: "Inverse Function Theorem (multivariable)"
description: "A C^1 map with invertible Jacobian at a point is locally a C^1 diffeomorphism"
---

**Inverse Function Theorem**: Let $U\subseteq\mathbb{R}^n$ be open and let $f:U\to\mathbb{R}^n$ be of {{< knowl id="class-ck-map" text="class" >}} $C^1$. Suppose $a\in U$ and
$
\det Df(a)\neq 0.
$
Let $b=f(a)$. Then there exist open {{< knowl id="neighborhood" text="neighborhoods" >}} $U_0$ of $a$ and $V_0$ of $b$ such that:
- $f:U_0\to V_0$ is {{< knowl id="bijective-function" section="shared-foundations" text="bijective" >}},
- the {{< knowl id="inverse-function" text="inverse" >}} $f^{-1}:V_0\to U_0$ is of class $C^1$, and
- the {{< knowl id="total-derivative-frechet-derivative" text="derivative" >}} of the inverse is given by
  $
  Df^{-1}(b) = (Df(a))^{-1},
  $
  and more generally $Df^{-1}(y)=(Df(f^{-1}(y)))^{-1}$ for $y\in V_0$.

This theorem is the rigorous foundation for local coordinate changes and for solving $f(x)=y$ locally when the linearization is invertible. See also {{< knowl id="diffeomorphism" text="diffeomorphism" >}}.
