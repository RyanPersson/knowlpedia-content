+++
id = "partial-differential-equations/finite-time-blowup"
title = "Finite-time blowup in a specified norm"
kind = "definition"
summary = "Unbounded growth of a chosen solution norm as time approaches a finite endpoint."
aliases = ["finite time blow-up", "norm blowup"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["linear-algebra/norm", "partial-differential-equations/maximal-existence-time", "real-analysis/limit-superior-at-an-endpoint"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(u(t)\) be a solution for \(t<T_*<\infty\). It has **finite-time blowup in the norm \(X\)** if
\[
\limsup_{t\uparrow T_*}\|u(t)\|_X=\infty.
\]
The [[real-analysis/limit-superior-at-an-endpoint|one-sided lim sup]], norm, and finite endpoint are part of the assertion. Some authors reserve “blowup” for the stronger statement that the norm tends to infinity; the convention should be stated.

## Different norms measure different losses

Blowup of a derivative norm need not mean blowup of the velocity itself. Conversely, a bounded spatial \(L^2\) norm does not bound the \(L^\infty\) norm: increasingly narrow peaks may grow in height while retaining bounded \(L^2\) mass.

## Breakdown and extension

Failure to extend a classical solution is often called breakdown. A continuation theorem can relate breakdown to the divergence of a specified norm or space-time integral, but that implication is additional mathematical information.

## Explicit continuation obstructions

An [[real-analysis/unbounded-path-prevents-continuous-extension|unbounded sequence approaching a finite space-time point]] rules out a continuous extension there. A [[partial-differential-equations/sobolev-continuation-obstruction|Sobolev embedding]] can separately rule out continuous extension in a specified Sobolev norm.
