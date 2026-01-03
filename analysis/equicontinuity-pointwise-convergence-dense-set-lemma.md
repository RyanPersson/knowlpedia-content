---
title: "Equicontinuity plus dense-set convergence implies uniform convergence on compacta"
description: "On a compact set, equicontinuity upgrades pointwise convergence on a dense set to uniform convergence"
---

**Lemma (equicontinuity + dense-set convergence)**: Let $K$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $(f_n)$ be a sequence of real-valued {{< knowl id="continuity-on-a-set" text="continuous" >}} functions on $K$ that is {{< knowl id="equicontinuity" text="equicontinuous" >}}: for every $\varepsilon>0$ there exists $\delta>0$ such that
$
d(x,y)<\delta \implies |f_n(x)-f_n(y)|<\varepsilon \quad \text{for all } n.
$
Assume there exists a {{< knowl id="dense-subset" text="dense" >}} subset $D\subseteq K$ such that for every $x\in D$, the sequence $(f_n(x))$ {{< knowl id="convergent-sequence" text="converges" >}} (equivalently, is {{< knowl id="cauchy-sequence" text="Cauchy" >}}).

Then $(f_n)$ is {{< knowl id="uniform-cauchy-sequence-of-functions" text="uniformly Cauchy" >}} on $K$, hence {{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="converges uniformly" >}} on $K$ to some continuous function $f$. Moreover, $f(x)=\lim_{n\to\infty} f_n(x)$ for all $x\in D$.

This lemma is a standard compactness-and-equicontinuity upgrade principle and is one of the key steps behind Arzelà–Ascoli-type arguments.
