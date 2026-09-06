+++
id = "real-analysis/riemann-additivity-over-subintervals"
title = "Additivity of the Riemann integral over subintervals"
kind = "knowl"
summary = "Splitting a Riemann integral at an interior point"
aliases = ["riemann-additivity-over-subintervals", "Additivity of the Riemann integral over subintervals"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/riemann-integrable-function", "real-analysis/interval"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 2
+++

Let \(f:[a,b]\to\mathbb R\) be [[real-analysis/riemann-integrable-function|Riemann integrable]] and let \(c\in[a,b]\). The restrictions of \(f\) to \([a,c]\) and \([c,b]\) are Riemann integrable, and
\[
\int_a^b f(x)\,dx=\int_a^c f(x)\,dx+\int_c^b f(x)\,dx.
\]

For \(c=a\) or \(c=b\), interpret the integral over the degenerate interval as zero.

## Example

Splitting at \(c=1\) gives
\[
\int_0^2 x\,dx=\int_0^1 x\,dx+\int_1^2 x\,dx=\tfrac12+\tfrac32=2.
\]

## References

- B. Yan, *The Riemann–Stieltjes Integral*, Definition 6.3 and Theorem 6.9(c), pp. 2 and 6–7 (specializing the integrator to \(\gamma(x)=x\)): [course notes PDF](https://users.math.msu.edu/users/yanb/327ch6.pdf).
