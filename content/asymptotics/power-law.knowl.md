+++
id = "asymptotics/power-law"
title = "Power law"
kind = "definition"
summary = "Dependence on a positive scale through a fixed real exponent."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["real-analysis/real-power", "shared-foundations/function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **power law** has the form \(f(s)=Cs^a\), where \(s>0\), \(C\ne0\), and \(a\in\mathbb R\) is fixed; \(s^a\) is the [[real-analysis/real-power|real power]]. It satisfies \(f(\lambda s)=\lambda^a f(s)\) for \(\lambda>0\).

## Asymptotic usage

An asymptotic power law \(f(s)\sim Cs^a\) uses [[asymptotics/asymptotic-equivalence|ratio convergence]]. The weaker estimate \(|f(s)|\asymp s^a\) specifies an order up to constants. As \(s\downarrow0\), positive exponents decay and negative exponents grow. Naming the scale matters: if \(s=\varepsilon^h\), then \(s^a=\varepsilon^{ha}\).
