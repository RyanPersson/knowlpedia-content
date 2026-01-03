---
title: "Heine–Cantor Theorem"
description: "Continuous functions on compact metric spaces are uniformly continuous"
---

**Heine–Cantor Theorem**: Let $(X,d_X)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $(Y,d_Y)$ be a metric space. If $f:X\to Y$ is {{< knowl id="continuity-on-a-set" text="continuous" >}}, then $f$ is {{< knowl id="uniform-continuity" text="uniformly continuous" >}} on $X$; i.e.,
$\forall \varepsilon>0\;\exists \delta>0\;\forall x,y\in X:\ d_X(x,y)<\delta \Rightarrow d_Y(f(x),f(y))<\varepsilon.$

This upgrades pointwise continuity to uniform control, and is essential for exchanging limits and integrals on compact domains and for approximation arguments.
