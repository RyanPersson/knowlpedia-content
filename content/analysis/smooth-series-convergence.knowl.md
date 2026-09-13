+++
id = "analysis/smooth-series-convergence"
title = "Smooth convergence of a series from derivative bounds"
kind = "theorem"
summary = "Summability of every compact derivative seminorm gives a smooth sum with termwise differentiation."
aliases = []
domains = ["analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/compact-derivative-seminorm", "real-analysis/uniform-convergence-differentiation", "real-analysis/weierstrass-m-test", "real-analysis/multi-index-notation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(f_j\in C^\infty(U)\), where \(U\subseteq\mathbb R^n\) is open. Suppose that for every compact \(K\subset U\) and every integer \(k\ge0\),
\[
\sum_j p_{K,k}(f_j)<\infty,
\]
with \(p_{K,k}\) the [[real-analysis/compact-derivative-seminorm|compact derivative seminorm]]. Then \(f=\sum_j f_j\) is smooth and
\[
\partial^\alpha f=\sum_j\partial^\alpha f_j
\]
locally uniformly for every multi-index \(\alpha\).

## Proof

The [[real-analysis/weierstrass-m-test|Weierstrass M-test]] gives uniform convergence of each derivative series on compact sets. Inside any closed rectangular box contained in \(U\), apply the one-variable [[real-analysis/uniform-convergence-differentiation|differentiation theorem]] along coordinate segments. Iterating identifies all the derivative limits. Such boxes cover \(U\).

## A diagonal sufficient condition

Let \((K_j)\) exhaust \(U\), with every compact subset eventually contained in \(K_j\). It suffices to arrange \(p_{K_j,j}(f_j)\le2^{-j}\) for all sufficiently large \(j\). For any fixed compact set and derivative order, the tail is then dominated by a geometric series; finitely many early terms cause no difficulty.
