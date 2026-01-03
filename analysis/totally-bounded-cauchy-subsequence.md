---
title: "Totally bounded iff every sequence has a Cauchy subsequence"
description: "A metric set admits finite ε-nets for all ε>0 exactly when sequences have Cauchy subsequences"
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $E\subseteq X$.

The set $E$ is **{{< knowl id="totally-bounded-set" text="totally bounded" >}}** if for every $\varepsilon>0$ there exist points $x_1,\dots,x_N\in X$ such that
$
E\subseteq \bigcup_{j=1}^N {{< knowl id="open-ball" text="$B$" >}}(x_j,\varepsilon).
$

**Proposition**: $E$ is totally bounded if and only if every sequence in $E$ has a {{< knowl id="cauchy-sequence" text="Cauchy" >}} {{< knowl id="subsequence" text="subsequence" >}}.

This proposition is the "sequential form" of total boundedness and is the key step in proving that {{< knowl id="compact-iff-complete-totally-bounded" text="complete + totally bounded implies compact" >}}.
