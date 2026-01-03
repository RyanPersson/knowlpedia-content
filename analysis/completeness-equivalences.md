---
title: "Completeness equivalences"
description: "Several standard statements are equivalent ways to express completeness of the real numbers"
---

The real numbers $\mathbb{R}$ are **{{< knowl id="complete-metric-space" text="complete" >}}**. In practice, completeness can be expressed in several equivalent ways.

**Completeness equivalences (standard list)**: The following statements are equivalent (each can be taken as a definition of completeness of $\mathbb{R}$):
- **Least upper bound property**: Every nonempty set $E\subseteq\mathbb{R}$ that is {{< knowl id="bounded-set" text="bounded" >}} above has a {{< knowl id="supremum" text="supremum" >}} in $\mathbb{R}$.
- **Cauchy completeness**: Every {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}} in $\mathbb{R}$ {{< knowl id="convergent-sequence" text="converges" >}} to a real number.
- **Nested interval property**: If $I_n=[a_n,b_n]$ are {{< knowl id="nested-interval-theorem" text="nested closed intervals" >}} with $I_{n+1}\subseteq I_n$ and $b_n-a_n\to 0$, then $\bigcap_{n=1}^\infty I_n$ consists of exactly one point.
- **Monotone convergence**: Every bounded {{< knowl id="monotone-sequence" text="monotone sequence" >}} in $\mathbb{R}$ converges.

These equivalences explain why different-looking arguments (suprema, Cauchy sequences, nested intervals, monotone sequences) are interchangeable in real analysis.
