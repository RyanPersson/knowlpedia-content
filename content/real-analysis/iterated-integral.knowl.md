+++
id = "real-analysis/iterated-integral"
title = "Iterated integral"
kind = "knowl"
summary = "A repeated one-variable integration over a rectangle or product of intervals."
aliases = ["iterated-integral", "Iterated integral"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/riemann-integral", "real-analysis/multiple-riemann-integral"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/iterated-integral.md"
+++

An **iterated integral** of \(f:[a,b]\times[c,d]\to\mathbb R\) integrates in one variable and then the other. The \(y\)-then-\(x\) iterated integral is
\[
\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx,
\]
provided that the inner [[real-analysis/riemann-integral|Riemann integral]] exists for every \(x\in[a,b]\) and the resulting function of \(x\) is Riemann integrable.

Iterated integrals are compared with the [[real-analysis/multiple-riemann-integral|multiple Riemann integral]]; under appropriate hypotheses they agree by [[real-analysis/fubini-theorem-riemann|Fubini's theorem (Riemann)]].

## Examples

- For \(f(x,y)=xy\) on \([0,1]^2\), the iterated integral is \(1/4\).
- If \(f(x,y)=g(x)h(y)\), then the iterated integral equals
  \[
  \left(\int_a^b g(x)\,dx\right)\left(\int_c^d h(y)\,dy\right)
  \]
  whenever the one-variable integrals exist.
