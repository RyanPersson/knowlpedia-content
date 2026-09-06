+++
id = "operator-algebras/tau-measurable-operator"
title = "Tau-measurable operator"
kind = "definition"
summary = "An affiliated closed operator whose domain is arbitrarily close to full in the measure determined by a semifinite trace."
aliases = ["τ-measurable operator", "trace-measurable operator"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/faithful-normal-semifinite-trace", "operator-algebras/affiliated-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) carry a
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] \(\tau\). A closed densely defined
[[operator-algebras/affiliated-operator|operator \(T\) affiliated with \(M\)]]
is **\(\tau\)-measurable** if its domain is \(\tau\)-dense: for every
\(\varepsilon>0\), there is a projection \(e\in M\) such that
\[
eH\subseteq\operatorname{dom}(T)
\quad\text{and}\quad
\tau(1-e)<\varepsilon.
\]
Thus the domain may omit a subspace, but the omitted projection can be made
arbitrarily small according to the chosen trace. The definition depends on
\(\tau\), not only on the underlying von Neumann algebra.

## Distribution-function characterization

The distribution function of \(T\) is
\[
d_T(s)=\tau\!\left(E^{|T|}((s,\infty))\right),\qquad s\geq0.
\]
The operator \(T\) is \(\tau\)-measurable exactly when
\(d_T(s)\to0\) as \(s\to\infty\). Indeed, the low-spectrum projections
\(E^{|T|}([0,s])\) provide bounded restrictions of \(T\), while their
complements have trace \(d_T(s)\). This criterion is the operator-algebraic
analogue of a [[measure-theory/measurable-function|measurable function]] being finite [[measure-theory/almost-everywhere|almost everywhere]].

## Measure topology and algebra

The \(\tau\)-measurable operators form an [[operator-algebras/involutive-algebra|involutive algebra]]
\(S(M,\tau)\) under closed sums and products. Its measure topology has basic
zero-neighborhoods consisting of operators \(T\) for which there is a
projection \(e\in M\) with
\[
\lVert Te\rVert\leq\varepsilon
\quad\text{and}\quad
\tau(1-e)\leq\delta.
\]
This algebra is complete for the measure topology. Generalized singular
numbers turn [[measure-theory/convergence-in-measure|convergence in measure]] into scalar estimates.

## Examples and distinctions

For \(M=L^\infty(X,\mu)\) with the integration trace,
\(S(M,\tau)\) identifies with the almost-everywhere finite measurable
functions, acting by multiplication. For \(B(H)\) with the usual operator
trace, every nonzero projection has trace at least one; taking
\(\varepsilon<1\) forces \(e=1\), so the \(\tau\)-measurable operators are
precisely the bounded operators.

**Warning.** Trace measurability is stronger than
[[operator-algebras/measurable-operator|\(M\)-measurability]] in general and
can change when the trace changes.

## References

1. Edward Nelson, “Notes on Non-Commutative Integration,” Journal of Functional Analysis 15 (1974), 103–116. [DOI record](https://doi.org/10.1016/0022-1236%2874%2990014-7). Relevant: pp. 103–116 on \(\tau\)-measurability and the measure topology.
2. Thierry Fack and Hideki Kosaki, “Generalized s-Numbers of \(\tau\)-Measurable Operators,” Pacific Journal of Mathematics 123 (1986), 269–300. [DOI record](https://doi.org/10.2140/pjm.1986.123.269). Relevant: §§1–3 on measure topology, distribution functions, and generalized singular numbers.
