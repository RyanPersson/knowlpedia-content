---
title: "Diffeomorphism"
description: "A bijective differentiable map whose inverse is also differentiable"
---

A **diffeomorphism** is a bijection $f:U\to V$ between {{< knowl id="open-set" section="topology" text="open sets" >}} $U,V\subseteq \mathbb{R}^n$ such that $f$ is differentiable on $U$ and the inverse map $f^{-1}:V\to U$ is differentiable on $V$.

A diffeomorphism is, in particular, a {{< knowl id="homeomorphism" section="topology" text="homeomorphism" >}}. Sufficient conditions for a map to be locally (and sometimes globally) a diffeomorphism are given by the {{< knowl id="inverse-function-theorem-rk" text="inverse function theorem" >}}, typically phrased using a nonzero {{< knowl id="jacobian-determinant" text="Jacobian determinant" >}}.

**Examples:**
- The translation $f(x)=x+a$ on $\mathbb{R}^n$ is a diffeomorphism with inverse $x\mapsto x-a$.
- Any invertible linear map $f(x)=Ax$ (with $\det A\ne 0$) is a diffeomorphism of $\mathbb{R}^n$.
