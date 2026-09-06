+++
id = "shared-foundations/factorial"
title = "Factorial"
kind = "knowl"
summary = "The product of all positive integers up to a given nonnegative integer."
aliases = ["factorial", "factorials"]
domains = ["shared-foundations"]
prerequisites = ["shared-foundations/natural-numbers", "shared-foundations/p-adic-valuation"]
dependency_review_count = 1
+++

For a [[shared-foundations/natural-numbers|natural number]] \(n\), the **factorial** of \(n\) is
\[
n!=\prod_{j=1}^{n}j=1\cdot2\cdots n,
\]
with the empty-product convention \(0!=1\). It satisfies the recursion \((n+1)!=(n+1)n!\).

Factorials encode the prime multiplicities accumulated in an initial interval. For a prime \(p\), Legendre's formula gives
\[
v_p(n!)=\sum_{r\ge1}\left\lfloor\frac{n}{p^r}\right\rfloor,
\]
where only finitely many summands are nonzero and \(v_p\) is the [[shared-foundations/p-adic-valuation|\(p\)-adic valuation]].
