---
title: "Lebesgue criterion for Riemann integrability"
description: "A bounded function is Riemann integrable iff its discontinuities form a measure-zero set"
---

**Lebesgue criterion for Riemann integrability**: Let $f:[a,b]\to\mathbb{R}$ be {{< knowl id="bounded-set" text="bounded" >}}, and let $D\subseteq[a,b]$ be the set of points where $f$ is discontinuous. Then $f$ is {{< knowl id="riemann-integrable-function" text="Riemann integrable" >}} on $[a,b]$ if and only if $D$ has {{< knowl id="set-of-measure-zero-in-rk" text="measure zero" >}}; i.e., for every $\varepsilon>0$ there exists a countable collection of open {{< knowl id="interval" text="intervals" >}} $\{I_j\}$ such that
$
D\subseteq \bigcup_{j=1}^\infty I_j
\quad\text{and}\quad
\sum_{j=1}^\infty |I_j|<\varepsilon.
$

This theorem is the complete structural characterization of Riemann integrability and explains exactly which discontinuity sets are allowed.
