---
title: "Convergent implies Cauchy"
description: "Every convergent sequence is Cauchy in any metric space"
---

**Convergent implies Cauchy**: Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $(x_n)$ be a sequence in $X$. If $x_n\to x$ for some $x\in X$, then $(x_n)$ is a {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}}:
$
\forall\varepsilon>0\;\exists N\;\forall m,n\ge N:\ d(x_n,x_m)<\varepsilon.
$

This lemma is a standard one-way implication in {{< knowl id="complete-metric-space" text="completeness" >}} arguments.
