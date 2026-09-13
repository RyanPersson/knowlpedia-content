+++
id = "asymptotics/asymptotic-expansion"
title = "Asymptotic expansion"
kind = "definition"
summary = "Approximation to every finite order in an asymptotic scale, without a convergence requirement."
aliases = ["Poincaré asymptotic expansion"]
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/asymptotic-scale", "asymptotics/little-o", "shared-foundations/finite-sum", "linear-algebra/normed-vector-space", "convex-analysis/seminorm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Given an [[asymptotics/asymptotic-scale|asymptotic scale]] \((\phi_j)\), the statement
\[
f(\varepsilon)\sim\sum_{j\ge0}a_j\phi_j(\varepsilon)
\]
means that for every fixed \(N\ge0\),
\[
f(\varepsilon)-\sum_{j=0}^N a_j\phi_j(\varepsilon)
=o(|\phi_N(\varepsilon)|).
\]
The sum in the defining estimate is finite. The infinite expression records all these estimates; it need not converge for any fixed \(\varepsilon\). For vector-valued coefficients the remainder is measured in a specified norm or family of seminorms.

## Recovering coefficients

The scale makes the coefficients unique: subtracting two expansions, the first unequal coefficient would give a nonzero limit after division by its scale function. A [[asymptotics/formal-expansion|formal expansion]] becomes an asymptotic expansion only after an actual function and the remainder bounds have been supplied.

## References

- [NIST Digital Library of Mathematical Functions, §2.1: Definitions and elementary properties](https://dlmf.nist.gov/2.1).
