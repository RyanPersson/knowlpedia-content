---
title: "Lebesgue Number Lemma"
description: "Every open cover of a compact metric space has a uniform radius so small balls lie in a single cover element"
---

**Lebesgue Number Lemma**: Let $(X,d)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $\mathcal{U}$ be an open cover of $X$. Then there exists $\delta>0$ (a **Lebesgue number** for $\mathcal{U}$) such that for every $x\in X$,
$B(x,\delta)\subseteq U \quad \text{for some } U\in\mathcal{U}.$

This lemma is used to pass from pointwise local control to uniform control on compact sets (e.g., in proofs of {{< knowl id="uniform-continuity" text="uniform continuity" >}} and partitions of unity in more advanced settings).
