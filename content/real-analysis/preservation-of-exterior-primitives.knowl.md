+++
id = "real-analysis/preservation-of-exterior-primitives"
title = "Preservation of exterior primitives by moment matching"
kind = "theorem"
summary = "Equal exterior sources and equal accumulated integrals give equal exterior primitives."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cumulative-weighted-integral", "real-analysis/weighted-radial-moment", "shared-foundations/function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose \(f_1=f_2\) for \(r\ge R_0>0\), and their weighted sources are integrable on \((0,R_0)\). If
\[
\int_0^{R_0}r^e(f_1-f_2)(r)\,dr=0,
\]
then their [[real-analysis/cumulative-weighted-integral|cumulative integrals]] from zero agree for every \(R\ge R_0\).

## Proof and parameter families

Split the difference of integrals at \(R_0\). The inner part vanishes by the moment condition and the outer part vanishes by equality of the sources. The argument applies componentwise to a finite family of sources, including nonlinear expressions in underlying profiles. If there are additional parameters, each matching condition must hold as an identity of those parameters. For primitives with prescribed additive constants, those constants must agree as well.
