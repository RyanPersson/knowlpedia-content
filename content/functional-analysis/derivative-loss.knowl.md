+++
id = "functional-analysis/derivative-loss"
title = "Derivative loss in an estimate"
kind = "definition"
summary = "An estimate requiring more derivatives of the input than it controls on the output."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/compact-derivative-seminorm", "functional-analysis/bounded-linear-operator"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An estimate for \(T\) has **loss of \(r\) derivatives** if controlling the output through order \(k\) requires input control through order \(k+r\), for example
\[
p_{K,k}(Tf)\le C_{K,k}\,p_{K',k+r}(f),
\]
where \(p_{K,k}\) is a [[real-analysis/compact-derivative-seminorm|derivative seminorm]]. The source and target spaces, sets \(K,K'\), and permitted dependence of \(C_{K,k}\) are part of the estimate.

## Example and a different use of loss

Differentiation \(D\) obeys \(\|Df\|_{C^k}\le\|f\|_{C^{k+1}}\). An inverse PDE operator may also lose derivatives if its estimate requires more regularity of the forcing than it returns for the solution.

A factor \(\varepsilon^{-r}\) in a parameter estimate is a loss of powers of a small scale, not necessarily a loss of differentiability. Both losses can occur together and must be tracked separately.
