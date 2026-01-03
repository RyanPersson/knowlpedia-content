---
title: "Arzelà–Ascoli Theorem"
description: "On a compact metric space, equicontinuity and pointwise boundedness characterize relative compactness in C(K)"
---

Let $(K,d)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and consider $C(K,\mathbb{R})$ with the {{< knowl id="sup-norm" text="sup metric" >}}
$
d_\infty(f,g)=\sup_{x\in K}|f(x)-g(x)|.
$

A subset $\mathcal{F}\subseteq C(K,\mathbb{R})$ is **{{< knowl id="relatively-compact-set" text="relatively compact" >}}** if its {{< knowl id="closure" text="closure" >}} in $(C(K,\mathbb{R}),d_\infty)$ is compact.

**Arzelà–Ascoli Theorem (real-valued, compact metric domain)**: For $\mathcal{F}\subseteq C(K,\mathbb{R})$, the following are equivalent:
- $\mathcal{F}$ is relatively compact in $(C(K,\mathbb{R}),d_\infty)$.
- $\mathcal{F}$ is {{< knowl id="equicontinuous-family" text="equicontinuous" >}} on $K$ and {{< knowl id="pointwise-bounded-family" text="pointwise bounded" >}} on $K$.

Equivalently (sequential form): $\mathcal{F}$ is relatively compact if and only if every sequence in $\mathcal{F}$ has a {{< knowl id="uniform-convergence" text="uniformly convergent" >}} {{< knowl id="subsequence" text="subsequence" >}} (with respect to $d_\infty$).

This theorem is the main compactness criterion for families of {{< knowl id="continuous-function" text="continuous functions" >}} and is central in existence proofs and approximation theory.
