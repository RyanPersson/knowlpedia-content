+++
id = "asymptotics/asymptotic-equivalence"
title = "Asymptotic equivalence"
kind = "definition"
summary = "A ratio tending to one in a stated limiting regime."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["real-analysis/limit-of-a-function-at-a-point", "shared-foundations/function", "asymptotics/little-o"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Functions \(f\) and \(g\), with \(g\ne0\) near the limiting point, are **asymptotically equivalent**, written \(f\sim g\), if the following [[real-analysis/limit-of-a-function-at-a-point|limit]] holds:
\[
\lim \frac{f}{g}=1.
\]
For real or complex functions this is equivalent to \(f-g=o(|g|)\), using [[asymptotics/little-o|little-o notation]]. The limiting variable and direction are part of the assertion.

## Distinguishing two conventions

Some authors use \(\sim\) for a two-sided bound. Here it always means ratio tending to one; [[asymptotics/comparable-functions|comparability]] is written \(\asymp\). For example, \(2\varepsilon\asymp\varepsilon\) but \(2\varepsilon\not\sim\varepsilon\).

## References

- [NIST Digital Library of Mathematical Functions, §2.1: Definitions and elementary properties](https://dlmf.nist.gov/2.1).
