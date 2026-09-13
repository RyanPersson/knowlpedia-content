+++
id = "asymptotics/finite-truncation"
title = "Finite truncation of an expansion"
kind = "definition"
summary = "The partial sum through a chosen order and its associated remainder."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/finite-sum", "asymptotics/asymptotic-scale"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **truncation through order \(N\)** of \(\sum_{j\ge0}a_j\phi_j(\varepsilon)\) is the finite sum
\[
S_N(\varepsilon)=\sum_{j=0}^N a_j\phi_j(\varepsilon).
\]
If an actual function \(f\) is specified, its remainder is \(R_N=f-S_N\). An [[asymptotics/asymptotic-scale|asymptotic scale]] orders the retained contributions by size.

## Meaning of an error bound

A [[asymptotics/asymptotic-expansion|full asymptotic expansion]] gives \(R_N=o(|\phi_N|)\) and, by using the next coefficient, \(R_N=O(|\phi_{N+1}|)\). Constants can depend on \(N\). A formal truncation by itself provides no bound on a remainder of an actual function.
