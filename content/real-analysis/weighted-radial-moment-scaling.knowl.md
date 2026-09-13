+++
id = "real-analysis/weighted-radial-moment-scaling"
title = "Scaling of weighted radial moments"
kind = "lemma"
summary = "The exact amplitude and length factors in a weighted one-dimensional radial integral."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/change-of-variables-formula", "real-analysis/real-power", "measure-theory/lebesgue-integrable-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(L>0\), let \(A\) be a scalar, put \(r=LR\), and define \(f_*(R)=Af(LR)\). If the weighted integrals are absolutely convergent, then for real \(e\),
\[
\int_0^\infty R^e f_*(R)\,dR
=AL^{-(e+1)}\int_0^\infty r^e f(r)\,dr.
\]
This is the [[real-analysis/change-of-variables-formula|change-of-variables formula]] including the radial differential \(dr=L\,dR\).

## Measure conventions

A cylindrical volume integral already contributes a factor \(r\); its exponent must be included in \(e\). For example, \(\int r f(r)\,dr\) acquires \(L^{-2}\), not \(L^{-1}\), when expressed in normalized variables with the above definition of \(f_*\). Parameters such as time are held fixed in this spatial substitution; differentiating them later also differentiates any parameter-dependent \(A\) and \(L\).
