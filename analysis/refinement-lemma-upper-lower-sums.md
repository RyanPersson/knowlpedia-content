---
title: "Refinement lemma for upper and lower sums"
description: "Refining a partition increases lower sums and decreases upper sums"
---

**Refinement lemma**: Let $f:[a,b]\to\mathbb{R}$ be {{< knowl id="bounded-set" text="bounded" >}}. If $P$ and $Q$ are {{< knowl id="partition-of-interval" text="partitions" >}} of $[a,b]$ and $Q$ is a {{< knowl id="refinement-of-a-partition" text="refinement" >}} of $P$ (i.e., every partition point of $P$ is also a partition point of $Q$), then
$
L(f,P)\le L(f,Q)\le U(f,Q)\le U(f,P),
$
where $L(f,P)$ and $U(f,P)$ are the {{< knowl id="lower-sum-riemann" text="lower" >}} and {{< knowl id="upper-sum-riemann" text="upper" >}} Riemann sums of $f$ with respect to $P$.

An analogous statement holds for Riemann–Stieltjes upper/lower sums when the integrator $\alpha$ is {{< knowl id="monotone-function" text="increasing" >}}.

This lemma formalizes the idea that making the partition finer can only improve the approximation: lower sums go up and upper sums go down.
