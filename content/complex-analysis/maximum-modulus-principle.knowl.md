+++
id = "complex-analysis/maximum-modulus-principle"
title = "Maximum modulus principle"
kind = "theorem"
summary = "A nonconstant holomorphic function cannot attain a local maximum of its modulus."
aliases = ["maximum modulus theorem"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/complex-domain", "complex-analysis/cauchy-integral-formula"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D\subseteq\mathbb C\) be a [[complex-analysis/complex-domain|domain]] and let \(f:D\to\mathbb C\) be holomorphic. If \(|f|\) has a local maximum at an interior point of \(D\), then \(f\) is constant on \(D\).

## Boundary form

If \(D\) is bounded, \(f\) is continuous on \(\overline D\), and holomorphic on \(D\), then
\[
\max_{\overline D}|f|=\max_{\partial D}|f|,
\]
unless \(f\) is constant. Compactness of \(\overline D\) ensures that the maximum exists; the local principle forces any nonconstant maximum to the boundary.

## Minimum modulus

Apply the principle to \(1/f\): if a holomorphic function has no zeros, \(|f|\) cannot attain an interior local minimum unless \(f\) is constant. A zero is an allowed minimum, so this statement requires the nonvanishing hypothesis.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 4, §3.
