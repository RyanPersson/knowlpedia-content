+++
id = "convex-analysis/indicator-function-of-a-set"
title = "Indicator function of a set"
kind = "knowl"
summary = "The extended-real function that is zero on a set and positive infinity outside it."
aliases = ["indicator-function-of-a-set", "Indicator function of a set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/indicator-function-of-a-set.md"
prerequisites = ["convex-analysis/extended-real-number-system-and-conventions", "convex-analysis/domain-and-epigraph-proper-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a set and let \(\Omega\subseteq X\). The **indicator function** of \(\Omega\) is the [[convex-analysis/extended-real-number-system-and-conventions|extended-real-valued]] function \(\delta_\Omega:X\to(-\infty,+\infty]\) defined by
\[
\delta_\Omega(x)=
\begin{cases}
0, & x\in\Omega,\\
+\infty, & x\notin\Omega.
\end{cases}
\]

Its effective [[convex-analysis/domain-and-epigraph-proper-function|domain]] is \(\operatorname{dom}(\delta_\Omega)=\Omega\), and its epigraph is \(\operatorname{epi}(\delta_\Omega)=\Omega\times[0,\infty)\).

## Remarks

Indicator functions encode constraints as penalties: minimizing \(f+\delta_\Omega\) is equivalent to minimizing \(f\) subject to \(x\in\Omega\).

When \(X\) is a real vector space, \(\delta_\Omega\) is [[convex-analysis/convex-function-via-epigraph|convex]] if and only if \(\Omega\) is a [[convex-analysis/convex-set|convex set]].
