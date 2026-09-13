+++
id = "asymptotics/leading-term"
title = "Leading term of an asymptotic expansion"
kind = "definition"
summary = "The first nonzero coefficient multiplied by its comparison function in an ordered expansion."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/asymptotic-expansion", "asymptotics/asymptotic-equivalence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If an [[asymptotics/asymptotic-expansion|asymptotic expansion]] has first nonzero coefficient \(a_k\), its **leading term** is \(a_k\phi_k\). For scalar coefficients,
\[
f(\varepsilon)=a_k\phi_k(\varepsilon)+o(|\phi_k(\varepsilon)|),
\qquad f\sim a_k\phi_k.
\]
The coefficient and comparison function together give the dominant approximation.

## Example

If \(f(\varepsilon)=3\varepsilon^2-\varepsilon^3+O(\varepsilon^4)\), the leading term is \(3\varepsilon^2\). An expansion with all coefficients zero has no first nonzero term; a nonzero flat function can have such an expansion.
