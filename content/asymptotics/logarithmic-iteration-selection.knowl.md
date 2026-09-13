+++
id = "asymptotics/logarithmic-iteration-selection"
title = "Logarithmic selection of an iteration level"
kind = "theorem"
summary = "A floor of a logarithm chooses an integer iterate whose size is comparable to a target scale."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/floor-function", "real-analysis/natural-logarithm", "real-analysis/real-power", "asymptotics/comparable-functions"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(T>1\), \(A\ge1\), and define \(i=\lfloor\log_T A\rfloor\), where \(\log_T A=(\log A)/(\log T)\). Then
\[
A/T<T^i\le A.
\]
The resulting quantities are [[asymptotics/comparable-functions|comparable]] with constants depending on the fixed base. This follows directly from \(i\le\log_T A<i+1\). For \(\Lambda>1\) and \(\rho=\log\Lambda/\log T\), it follows that
\[
\Lambda^{-1}A^\rho<\Lambda^i\le A^\rho.
\]
The integer iterate therefore matches the desired size up to fixed multiplicative constants.

## Neighboring levels

For two positive targets \(A,B\ge1\), their selected levels obey
\[
|i(A)-i(B)|\le1+\frac{|\log(A/B)|}{\log T}.
\]
Thus a uniform bound on target ratios gives a uniform bound on level differences. The level is discrete and locally constant except at threshold values; no derivative of the floor function is used in smooth coordinate estimates.
