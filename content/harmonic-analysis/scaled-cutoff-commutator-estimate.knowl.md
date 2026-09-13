+++
id = "harmonic-analysis/scaled-cutoff-commutator-estimate"
title = "Scaled cutoff commutator estimate"
kind = "theorem"
summary = "A scale-R Lipschitz cutoff gives an L1 to Lq commutator bound below the first-order endpoint."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/multiplication-commutator-kernel", "harmonic-analysis/young-convolution-inequality", "real-analysis/change-of-variables-formula", "real-analysis/chain-rule-multivariable", "topology/lipschitz-continuity", "measure-theory/lp-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(n\ge2\), let \(T=cI+\operatorname{p.v.}K\) have kernel bounded by \(C|x-y|^{-n}\), and let \(a_R(x)=a(x/R)\) with \(a\) bounded and Lipschitz. For
\[
1<q<\frac n{n-1},
\]
the [[harmonic-analysis/multiplication-commutator-kernel|multiplication commutator]] extends from smooth compactly supported inputs to \(L^1\), and
\[
\|[M_{a_R},T]f\|_q\le C_{a,n,q}R^{-n+n/q}\|f\|_1.
\]
The constant also depends on the kernel bound and is independent of \(R>0\) and \(f\).

## Integrable majorant

The commutator kernel is dominated by
\[
k_R(z)=C|z|^{-n}\min(|z|/R,1).
\]
Its \(L^q\) norm is finite at zero if \(q<n/(n-1)\), and at infinity if \(q>1\). Rescaling \(z=Rz'\) gives \(\|k_R\|_q=C R^{-n+n/q}\). Young's convolution inequality proves the result and its unique extension. In \(n=3\), choosing \(q=4/3\) gives \(C R^{-3/4}\|f\|_1\).

For an \(L^1\) input the notation denotes this integral extension; individual terms \(a_RT f\) and \(T(a_Rf)\) need their own interpretation.
