+++
id = "analysis/locally-finite-smooth-sum"
title = "Locally finite sum of smooth functions"
kind = "theorem"
summary = "A family with locally finite supports may be summed and differentiated as a finite sum near each point."
aliases = []
domains = ["analysis"]
section_mode = "progressive"
prerequisites = ["topology/locally-finite-family", "real-analysis/class-ck-map", "shared-foundations/support-of-a-function", "real-analysis/multi-index-notation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \((f_j)_{j\in J}\) be smooth functions on an open set \(U\subseteq\mathbb R^n\). If their supports form a [[topology/locally-finite-family|locally finite family]], then
\[
f(x)=\sum_{j\in J}f_j(x)
\]
is smooth and \(\partial^\alpha f=\sum_j\partial^\alpha f_j\). Each point has a neighborhood on which only finitely many terms can be nonzero, so both statements reduce there to finite sums.

## Local finiteness versus bounded overlap

Bounded overlap is a pointwise multiplicity bound and does not supply such a neighborhood. For example, choose disjoint bump functions of height one in intervals \((2^{-j},2^{-j}+2^{-j-2})\). Their supports have multiplicity at most one, but accumulate at zero. Their sum, with value zero at zero, is not continuous there.

If supports accumulate at a boundary, smoothness across that boundary instead requires control of derivative tails, as in [[analysis/smooth-series-convergence|smooth series convergence]].
