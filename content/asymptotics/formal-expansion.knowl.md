+++
id = "asymptotics/formal-expansion"
title = "Formal expansion"
kind = "definition"
summary = "A sequence of coefficients manipulated order by order without asserting analytic convergence."
aliases = ["formal power expansion"]
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/sequence", "shared-foundations/finite-sum", "algebra-rings/polynomial-ring"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **formal expansion** \(\sum_{j\ge0}\varepsilon^j a_j\) specifies a [[shared-foundations/sequence|sequence]] of coefficients and an indeterminate \(\varepsilon\). Addition is coefficientwise; when coefficients can be multiplied, multiplication uses
\[
(ab)_n=\sum_{j=0}^n a_jb_{n-j}.
\]
Each output coefficient is a finite sum. No numerical value of \(\varepsilon\), convergence, or underlying function is asserted.

## Equations order by order

Substitution into a polynomial equation and comparison of coefficients can recursively determine the \(a_j\). A finite differential polynomial admits the same procedure with coefficient functions and their derivatives. Producing a function with this formal expansion requires an additional realization or remainder argument; an [[asymptotics/asymptotic-expansion|asymptotic expansion]] states that analytic conclusion.
