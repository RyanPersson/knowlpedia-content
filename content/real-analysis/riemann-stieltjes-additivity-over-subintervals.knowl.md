+++
id = "real-analysis/riemann-stieltjes-additivity-over-subintervals"
title = "Additivity of the Riemann–Stieltjes integral over subintervals"
kind = "knowl"
summary = "Splitting a Riemann–Stieltjes integral at an interior point"
aliases = ["riemann-stieltjes-additivity-over-subintervals", "Additivity of the Riemann–Stieltjes integral over subintervals"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/riemann-stieltjes-integral", "real-analysis/monotone-function"]
dependency_review_count = 1
+++

Suppose \(\gamma:[a,b]\to\mathbb R\) is [[real-analysis/monotone-function|increasing]] and \(f:[a,b]\to\mathbb R\) is [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes integrable]] with respect to \(\gamma\). If \(c\in[a,b]\), then the restrictions of \(f\) and \(\gamma\) to the two subintervals are integrable in the same sense, and
\[
\int_a^b f\,d\gamma=\int_a^c f\,d\gamma+\int_c^b f\,d\gamma.
\]

At an endpoint, the integral over the degenerate interval is defined to be zero.

## Why the split works

For the mesh-limit definition used here, compare two fine tagged partitions on
one subinterval while keeping the same fine partition on the other. The Cauchy
criterion for the full integral implies the Cauchy criterion for each restricted
integral. Combining fine partitions then gives the displayed sum. The cited
reference states the increasing-integrator case using upper and lower sums;
its formulation should not be substituted for the mesh-limit definition without
checking the integrator's discontinuities.

## References

- B. Yan, *The Riemann–Stieltjes Integral*, Theorem 6.9(c), pp. 6–7: [course notes PDF](https://users.math.msu.edu/users/yanb/327ch6.pdf).
