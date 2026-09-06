+++
id = "operator-algebras/operator-trace"
title = "Canonical operator trace"
kind = "definition"
summary = "The basis-independent extended sum of diagonal matrix coefficients of a positive Hilbert-space operator."
aliases = ["trace on positive operators", "Hilbert-space trace", "Tr"]
domains = ["operator-algebras"]
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/orthonormal-basis", "real-analysis/partial-sums"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]] and let \(T\) be
a positive bounded operator on \(H\). Its **canonical operator trace** is
\[
\operatorname{Tr}(T)=\sum_{e\in\mathcal E}\langle Te,e\rangle\in[0,\infty],
\]
where \(\mathcal E\) is any [[linear-algebra/orthonormal-basis|orthonormal basis]] and an arbitrary nonnegative sum
means the supremum of its finite [[real-analysis/partial-sums|partial sums]]. The value is independent of
\(\mathcal E\). If it is finite, \(T\) is trace class. For a general
trace-class operator \(S\), the series
\(\operatorname{Tr}(S)=\sum_{e\in\mathcal E}\langle Se,e\rangle\) converges
absolutely and is likewise basis independent. Thus the positive trace may
take \(+\infty\), while the linear trace is defined on the trace-class ideal.

## Relation to singular values

A [[linear-algebra/compact-operator|compact operator]] \(S\) is trace class exactly when
\[
\sum_{n=1}^{\infty}s_n(S)<\infty,
\]
where \(s_n(S)\) are its
[[functional-analysis/singular-values|singular values]]. In that case
\(\operatorname{Tr}(|S|)=\sum_ns_n(S)\) and
\(|\operatorname{Tr}(S)|\leq\operatorname{Tr}(|S|)\). For a positive compact
operator, the trace is the sum of its eigenvalues counted with multiplicity.

## Tracial and continuity properties

If \(S\) is trace class and \(A\) is bounded, then both \(AS\) and \(SA\) are
trace class and
\[
\operatorname{Tr}(AS)=\operatorname{Tr}(SA).
\]
The trace is positive, faithful on positive operators, and normal: increasing
nets of positive operators have traces increasing to the trace of their
supremum. Cyclicity must not be applied indiscriminately to products of
unbounded operators; the trace-class hypotheses are what make the displayed
identity valid.

## Scope and normalizations

On \(B(H)\), this trace assigns value one to every rank-one projection and is
the canonical [[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]]. Other operator algebras may
carry no trace, one trace, or many traces, and a normalized [[operator-algebras/tracial-state|tracial state]] is a
different notion. In finite dimension, the definition reduces to the ordinary
matrix trace. In infinite dimension, \(\operatorname{Tr}(I)=+\infty\), so the
canonical trace is not a state.

## References

1. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., American Mathematical Society, 2005. [DOI record](https://doi.org/10.1090/surv/120). Relevant: §§1–3 on trace-class operators, singular values, and cyclicity.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [Publisher record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VI on trace ideals and the canonical trace.
