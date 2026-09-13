+++
id = "measure-theory/ordered-integration-simplex"
title = "Ordered integration simplex"
kind = "calculation"
summary = "The region of ordered times in an interval, whose volume is the interval length to the nth power divided by n factorial."
aliases = ["time-ordered simplex", "integration simplex"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-measure", "measure-theory/fubinis-theorem", "shared-foundations/factorial"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(s<t\), the **ordered integration simplex** is
\[
\{(t_1,\ldots,t_n):s<t_n<\cdots<t_1<t\}.
\]
Its volume is \((t-s)^n/n!\). Up to the measure-zero sets where coordinates coincide, the cube \((s,t)^n\) splits into \(n!\) congruent regions, one per coordinate ordering; dividing its volume proves the formula.

## Iterated-integral bound

If \(\|A(\tau)\|\le M\), submultiplicativity of the operator norm gives
\[
\left\|\int_{s<t_n<\cdots<t_1<t}A(t_1)\cdots A(t_n)\,dt_n\cdots dt_1\right\|
\le\frac{(M(t-s))^n}{n!}.
\]
The factorial records time ordering and makes the resulting series converge on every finite interval.
