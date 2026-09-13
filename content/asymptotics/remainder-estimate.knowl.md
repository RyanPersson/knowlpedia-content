+++
id = "asymptotics/remainder-estimate"
title = "Remainder estimate"
kind = "definition"
summary = "A quantitative error bound after subtracting a stated approximation."
aliases = ["error estimate", "higher-order remainder", "higher-order correction"]
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["linear-algebra/normed-vector-space", "asymptotics/big-o", "asymptotics/finite-truncation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an approximation \(S_\varepsilon\) to \(F_\varepsilon\), a **remainder estimate** bounds \(R_\varepsilon=F_\varepsilon-S_\varepsilon\), for example
\[
\|R_\varepsilon\|_X\le C\varepsilon^a.
\]
It must identify the [[linear-algebra/normed-vector-space|norm]] or seminorm, the parameter range, exponent, and constant dependencies. In an expansion, \(S_\varepsilon\) can be a [[asymptotics/finite-truncation|finite truncation]].

## Higher order and flat errors

Relative to a nonzero term of order \(\varepsilon^b\), an error bound with \(a>b\) is higher order. An error is flat in the parameter if, for every \(N\), it is \(O(\varepsilon^N)\) in the specified topology. A single positive-order bound does not imply flatness, nor does a value bound imply estimates for derivatives.
