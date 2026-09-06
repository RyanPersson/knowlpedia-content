+++
id = "real-analysis/uniform-continuity-preserves-cauchy"
title = "Uniform continuity preserves Cauchy sequences"
kind = "knowl"
summary = "Uniformly continuous maps send Cauchy sequences to Cauchy sequences"
aliases = ["uniform-continuity-preserves-cauchy", "Uniform continuity preserves Cauchy sequences"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-continuity-preserves-cauchy.md"
prerequisites = ["real-analysis/uniform-continuity", "topology/cauchy-sequence"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

Let \((X,d_X)\) and \((Y,d_Y)\) be [[topology/metric-space|metric spaces]] and let \(f:X\to Y\) be [[real-analysis/uniform-continuity|uniformly continuous]].

**Proposition.** If \((x_n)\) is a [[topology/cauchy-sequence|Cauchy sequence]] in \(X\), then \((f(x_n))\) is a Cauchy sequence in \(Y\).

Indeed, given \(\varepsilon>0\), choose \(\delta>0\) from uniform continuity. For all sufficiently large \(m,n\), the Cauchy property gives \(d_X(x_m,x_n)<\delta\), hence \(d_Y(f(x_m),f(x_n))<\varepsilon\).

Continuity alone does not suffice: \(f(x)=1/x\) on \((0,1)\) sends the Cauchy sequence \(x_n=1/n\) to the non-Cauchy sequence \(n\).
