+++
id = "asymptotics/diagonal-choice-of-shrinking-scales"
title = "Diagonal choice of shrinking scales"
kind = "theorem"
summary = "Finitely many vanishing requirements at each stage can be met by one geometrically shrinking sequence."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/logarithmic-loss-absorption", "shared-foundations/recursion-on-natural-numbers", "asymptotics/parameter-choice-hierarchy"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

At each integer stage \(j\ge1\), let a finite list of functions \(h_{j,k}(q)\) satisfy \(h_{j,k}(q)\to0\) as \(q\downarrow0\). Given \(q_0>0\), one can choose \(a_1^{-1}<q_0\) and \(a_{j+1}\ge2a_j\) such that
\[
|h_{j,k}(q)|\le2^{-j}\qquad(0<q\le a_j^{-1})
\]
for every requirement at stage \(j\). This is a **diagonal scale choice** by [[shared-foundations/recursion-on-natural-numbers|recursion]].

## Why finitely many requirements suffice

For each fixed stage, every requirement holds throughout some sufficiently small interval. The minimum of finitely many positive thresholds is positive. Choose \(a_j\) beyond its reciprocal and beyond the previous geometric-growth requirement. For example, \(h_{j,k}=C_{j,k}q^{\gamma_{j,k}}(1+|\log q|)^{P_{j,k}}\), with \(\gamma_{j,k}>0\), tends to zero. Arbitrarily large stage constants are allowed; their size affects the chosen cutoff scale.

Imposing all derivative orders at a single stage would generally give infinitely many conditions and is not justified by this argument. Instead, stage \(j\) can cover orders at most \(j\), so every fixed order is eventually covered.
