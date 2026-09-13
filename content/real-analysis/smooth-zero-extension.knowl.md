+++
id = "real-analysis/smooth-zero-extension"
title = "Smooth zero extension across a flat boundary"
kind = "theorem"
summary = "Locally uniform vanishing of every mixed derivative permits smooth extension by zero."
aliases = ["zero extension", "flat endpoint extension"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/smooth-extension", "real-analysis/flat-function", "real-analysis/multi-index-notation", "real-analysis/fundamental-theorem-of-calculus-i"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(U\subseteq\mathbb R^n\) be open and \(f\in C^\infty(U\times(0,\varepsilon))\). Suppose that for every compact \(K\subset U\), multi-index \(\alpha\), and integer \(k\ge0\),
\[
\sup_{x\in K}|\partial_x^\alpha\partial_t^k f(x,t)|\longrightarrow0
\quad(t\downarrow0).
\]
Then setting \(F(x,t)=f(x,t)\) for \(t>0\) and \(F(x,t)=0\) for \(t\le0\) defines a [[real-analysis/smooth-extension|smooth extension]] on \(U\times(-\varepsilon,\varepsilon)\). It is [[real-analysis/flat-function|flat]] on \(U\times\{0\}\).

## Why the mixed derivatives suffice

Extend each proposed derivative by zero. The hypothesis makes these extensions continuous near every boundary point. For the normal derivative, the fundamental theorem of calculus gives
\[
f(x,t)=\int_0^t\partial_t f(x,s)\,ds,
\]
by first integrating from \(\delta>0\) and passing to \(\delta\downarrow0\). The resulting difference quotient has the asserted limit. Tangential difference quotients on the boundary are zero. Repeat this argument for each extended derivative.

## Necessary condition

If an extension is smooth and identically zero for \(t<0\), all of its derivatives vanish on \(t=0\). Continuity on compact sets yields the locally uniform limits above. Merely having \(f(x,t)\to0\) does not control its derivatives.
