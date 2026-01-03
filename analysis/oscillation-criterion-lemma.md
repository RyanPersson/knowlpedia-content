---
title: "Oscillation criterion lemma"
description: "Upper minus lower sum equals the oscillation sum, yielding a practical integrability criterion"
---

Let $f:[a,b]\to\mathbb{R}$ be {{< knowl id="bounded-set" text="bounded" >}}. For a subinterval $I\subseteq[a,b]$, define the **{{< knowl id="oscillation-of-a-function" text="oscillation" >}} of $f$ on $I$** by
$
\omega(f;I)=\sup_{x\in I} f(x)-\inf_{x\in I} f(x)\ \in[0,\infty),
$
where {{< knowl id="supremum" text="sup" >}} and {{< knowl id="infimum" text="inf" >}} denote the {{< knowl id="least-upper-bound-theorem" text="supremum and infimum" >}}.

**Oscillation identity**: If $P=\{a=x_0<x_1<\cdots<x_n=b\}$ is a {{< knowl id="partition-of-interval" text="partition" >}}, then
$
U(f,P)-L(f,P)=\sum_{i=1}^n \omega\bigl(f;[x_{i-1},x_i]\bigr)\,(x_i-x_{i-1}).
$

**Oscillation criterion (Riemann integrability)**: A bounded function $f$ is {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} on $[a,b]$ if and only if for every $\varepsilon>0$ there exists a partition $P$ such that
$
\sum_{i=1}^n \omega\bigl(f;[x_{i-1},x_i]\bigr)\,(x_i-x_{i-1})<\varepsilon.
$

This criterion repackages $U(f,P)-L(f,P)$ into a concrete "local oscillation" quantity and is a standard starting point for proving integrability of classes of functions.
