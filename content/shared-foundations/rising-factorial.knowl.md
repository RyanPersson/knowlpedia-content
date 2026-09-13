+++
id = "shared-foundations/rising-factorial"
title = "Rising factorial"
kind = "definition"
summary = "The product a(a+1)...(a+n-1), including the empty product at n=0."
aliases = ["Pochhammer symbol", "rising factorials"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/complex-numbers-c", "shared-foundations/finite-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(a\in\mathbb C\) and a nonnegative integer \(n\), the **rising factorial** is
\[
(a)_0=1,\qquad
(a)_n=\prod_{j=0}^{n-1}(a+j).
\]
The same notation is also called the **Pochhammer symbol**; some conventions use an upward arrow to distinguish it from a falling factorial. It satisfies
\[
(a)_{n+1}=(a+n)(a)_n,\qquad
(a)_{m+n}=(a)_m(a+m)_n.
\]

## Examples

\((1)_n=n!\), whereas \((a)_2=a(a+1)\). The definition is a polynomial in \(a\); it therefore remains meaningful at parameters where a quotient of gamma functions used to represent it would contain poles.
