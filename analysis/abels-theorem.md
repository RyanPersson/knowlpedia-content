---
title: "Abel's Theorem (power series at x=1)"
description: "If a series sum a_n converges, then sum a_n r^n tends to the same limit as r→1−"
---

**Abel's Theorem (one standard form)**: Let $(a_n)$ be a real or complex sequence such that the {{< knowl id="series" text="series" >}} $\sum_{n=0}^\infty a_n$ {{< knowl id="convergent-series" text="converges" >}} to $s$. For $0\le r<1$, define
$
f(r)=\sum_{n=0}^\infty a_n r^n,
$
which converges for $|r|<1$. Then
$
\lim_{r\to 1^-} f(r)=s.
$

This theorem connects ordinary convergence of $\sum a_n$ to the boundary behavior of the associated power series with radius $1$. It is one of the basic results explaining why power series behave well as the variable approaches the boundary from within.
