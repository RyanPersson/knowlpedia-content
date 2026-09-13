+++
id = "harmonic-analysis/gaussian-pulse-envelope"
title = "Gaussian bound from a decreasing net growth rate"
kind = "lemma"
summary = "A growth rate with uniformly negative slope yields a Gaussian envelope about its zero."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/pulse-envelope", "real-analysis/newton-leibniz-formula", "real-analysis/taylors-theorem-with-remainder"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(g\in C^1([0,L])\), \(L>0\), satisfy \(g(L/2)=0\) and
\[
-C/L\le g'(v)\le-c/L\qquad(0<c\le C).
\]
For the [[harmonic-analysis/pulse-envelope|envelope]] \(P(v)=\exp(\int_{L/2}^v g(s)\,ds)\),
\[
\exp\left(-\frac{C(v-L/2)^2}{2L}\right)
\le P(v)\le
\exp\left(-\frac{c(v-L/2)^2}{2L}\right)\le1.
\]

## Proof and endpoint decay

The function \(h=\log P\) satisfies \(h(L/2)=h'(L/2)=0\) and \(-C/L\le h''\le-c/L\). Integrating twice, or applying Taylor's theorem with integral remainder, gives the bounds on either side of the midpoint. In particular, \(P(0),P(L)\le e^{-cL/8}\). A cutoff varying only in endpoint regions a fixed proportion away from the midpoint acts where \(P\le e^{-c' L}\), for a fixed \(c'>0\).
