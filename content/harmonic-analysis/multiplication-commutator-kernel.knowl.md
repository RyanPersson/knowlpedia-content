+++
id = "harmonic-analysis/multiplication-commutator-kernel"
title = "Kernel cancellation in a multiplication commutator"
kind = "theorem"
summary = "Commuting a singular integral with multiplication introduces a difference of coefficients."
aliases = ["cutoff commutator identity"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/operator-commutator", "functional-analysis/multiplication-operator", "harmonic-analysis/principal-value-singular-integral", "topology/lipschitz-continuity", "functional-analysis/test-function-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Suppose \(T=cI+\operatorname{p.v.}K\) is a singular integral with \(|K(x,y)|\le C|x-y|^{-n}\), and let \(a\) be bounded and Lipschitz. For compactly supported smooth \(f\), its [[functional-analysis/operator-commutator|commutator]] with multiplication is
\[
[M_a,T]f(x)=a(x)Tf(x)-T(af)(x)
=\int(a(x)-a(y))K(x,y)f(y)\,dy.
\]
The integral is absolutely convergent, and the local term \(cI\) cancels.

## Gain at the diagonal

Lipschitz continuity gives \(|a(x)-a(y)|\le C_a|x-y|\), so the new kernel is bounded by \(C C_a|x-y|^{1-n}\) near the diagonal, an integrable singularity. Boundedness of \(a\) controls the remaining region. The identity follows first for truncated integrals and then by dominated convergence.
