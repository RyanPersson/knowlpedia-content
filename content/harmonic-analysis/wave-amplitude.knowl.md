+++
id = "harmonic-analysis/wave-amplitude"
title = "Wave amplitude"
kind = "definition"
summary = "The scalar or vector coefficient multiplying an oscillatory phase factor."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/oscillatory-phase", "shared-foundations/complex-conjugate", "linear-algebra/vector-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In an oscillatory field
\[
w(t,x)=a(t,x)e^{i\kappa\Phi(t,x)},
\]
the coefficient \(a\) multiplying the [[harmonic-analysis/oscillatory-phase|phase factor]] is the **amplitude**. It may be a complex scalar or vector. For real-valued fields one often takes \(\operatorname{Re}(ae^{i\kappa\Phi})\) or the conjugate pair \(ae^{i\kappa\Phi}+\bar a e^{-i\kappa\Phi}\); these conventions differ by a factor of two.

## Separation assumptions

Calling \(a\) an amplitude does not imply it varies slowly. Relative derivative bounds must be supplied. The decomposition also depends on convention: a phase factor can be moved between \(a\) and the [[harmonic-analysis/oscillatory-phase|phase]] unless a choice has been fixed. An envelope is a bound on an amplitude, not necessarily the amplitude itself.
