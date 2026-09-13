+++
id = "asymptotics/perturbation"
title = "Perturbation"
kind = "definition"
summary = "A change from a reference object, with smallness measured in a stated space or parameter."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["linear-algebra/normed-vector-space", "asymptotics/big-o"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a reference element \(u_0\) in a [[linear-algebra/normed-vector-space|normed vector space]], a **perturbation** is an increment \(h\), giving the modified object \(u=u_0+h\). A family is a small perturbation in that norm if \(\|h_\varepsilon\|\to0\); a quantitative version is \(\|h_\varepsilon\|=O(\varepsilon^a)\) with \(a>0\).

## The chosen topology matters

For functions, small values do not imply small derivatives. For example, \(\varepsilon\sin(x/\varepsilon)\) tends uniformly to zero while its first derivative does not. Perturbation arguments must name the norm, derivative seminorms, or weighted estimates used. An increment can be small relative to a growing reference field without being absolutely small.
