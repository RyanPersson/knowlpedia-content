+++
id = "real-analysis/even-and-odd-functions"
title = "Even and odd parity of a function"
kind = "definition"
summary = "The transformation rules f(-x)=f(x) and f(-x)=-f(x) on a reflection-invariant domain."
aliases = ["parity of a function", "even function", "odd function"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

On a domain invariant under \(x\mapsto-x\), a scalar [[shared-foundations/function|function]] has **even parity** if \(f(-x)=f(x)\), and **odd parity** if \(f(-x)=-f(x)\). These are the two sign characters of reflection. Every function on such a domain splits uniquely as
\[
f(x)=\frac{f(x)+f(-x)}2+\frac{f(x)-f(-x)}2,
\]
an even part plus an odd part.

## Calculus

Differentiation interchanges these parities. Products multiply their signs: odd times odd is even. If an odd function is integrable on a symmetric interval, its integral is zero. Parity in one coordinate means reflecting that coordinate while holding all others fixed; for vector fields, the transformation of the basis also matters.
