+++
id = "asymptotics/logarithmic-loss-absorption"
title = "Absorbing logarithmic losses into a power"
kind = "lemma"
summary = "Every fixed power of a logarithm grows more slowly than any negative power of a small parameter."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function", "real-analysis/natural-logarithm", "real-analysis/real-power", "asymptotics/little-o"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For fixed \(a>0\) and \(m\ge0\),
\[
\varepsilon^a(1+|\log\varepsilon|)^m\longrightarrow0
\qquad(\varepsilon\downarrow0).
\]
Consequently, for \(b<a\),
\[
\varepsilon^a(1+|\log\varepsilon|)^m=o(\varepsilon^b).
\]
The [[real-analysis/natural-logarithm|logarithmic]] factor can be absorbed by spending an arbitrarily small positive amount of power.

## Proof and uniformity

Put \(s=-\log\varepsilon\). The expression becomes \(e^{-as}(1+s)^m\). Choose an integer \(n>m\) and use \(e^{as/2}\ge(as/2)^n/n!\); the resulting bound tends to zero. Constants depend on \(a,m\). The conclusion does not give a common threshold for unbounded \(m\) without extra information.
