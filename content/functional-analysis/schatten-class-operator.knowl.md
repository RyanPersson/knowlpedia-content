+++
id = "functional-analysis/schatten-class-operator"
title = "Schatten-class operator"
kind = "definition"
summary = "A compact Hilbert-space operator whose singular-value sequence is summable to a specified power."
aliases = ["Schatten p-class", "Schatten ideal"]
domains = ["functional-analysis", "operator-algebras"]
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/compact-operator", "functional-analysis/singular-values", "algebra-rings/two-sided-ideal"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(H\) and \(K\) be [[linear-algebra/hilbert-space|Hilbert spaces]] and let
\(0<p<\infty\). A **Schatten-class operator of order \(p\)** is a
[[linear-algebra/compact-operator|compact operator]] \(T:H\to K\) whose
[[functional-analysis/singular-values|singular values]] satisfy
\[
\sum_{n\geq 1}s_n(T)^p<\infty.
\]
The space of all such operators is denoted \(\mathcal S^p(H,K)\), or
\(\mathcal L^p(H,K)\), and carries the norm or quasinorm
\[
\lVert T\rVert_p=\left(\sum_{n\geq1}s_n(T)^p\right)^{1/p}.
\]
It is a norm when \(p\geq1\) and a quasinorm when \(0<p<1\). When \(H=K\),
\(\mathcal S^p(H)\) is a [[algebra-rings/two-sided-ideal|two-sided ideal]] in the bounded operators on \(H\).
Thus Schatten membership is a quantitative compactness condition.

## Ideal and inclusion properties

If \(A\) and \(B\) are bounded operators of compatible sizes and
\(T\in\mathcal S^p\), then
\[
\lVert ATB\rVert_p\leq\lVert A\rVert\,\lVert T\rVert_p\,\lVert B\rVert.
\]
For \(0<p<q<\infty\), one has
\(\mathcal S^p\subseteq\mathcal S^q\subseteq\mathcal K\). Hölder's inequality
also has an operator-ideal form: if \(1/r=1/p+1/q\), then products of
\(\mathcal S^p\)- and \(\mathcal S^q\)-operators lie in
\(\mathcal S^r\), with the usual qualification \(r\geq1\) when a Banach norm
is desired.

## Distinguished cases

The class \(\mathcal S^1\) is the trace class, and \(\mathcal S^2\) is the
Hilbert--Schmidt class. For a diagonal compact operator on \(\ell^2\) with
diagonal \((\lambda_n)\), membership in \(\mathcal S^p\) is exactly the
condition \((\lambda_n)\in\ell^p\). [[functional-analysis/finite-rank-operator|Finite-rank operators]] belong to every
\(\mathcal S^p\) and are dense there in the \(p\)-norm.

## Conventions and scope

For \(0<p<1\), “Schatten class” is sometimes replaced by “quasi-Schatten
ideal” to emphasize the lack of a norm. Some authors extend the notation by setting
\(\mathcal S^\infty(H)=\mathcal K(H)\) with the [[linear-algebra/operator-norm|operator norm]]. Others reserve
“Schatten class” for finite \(p\), as in the core definition. These
conventions should be stated when endpoints or subunit exponents matter.

## References

1. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., American Mathematical Society, 2005. [DOI record](https://doi.org/10.1090/surv/120). Relevant: Chapters 1--2 on singular values, Schatten ideals, and ideal inequalities.
