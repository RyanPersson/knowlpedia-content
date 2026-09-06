+++
id = "real-analysis/oscillation"
title = "Oscillation"
kind = "knowl"
summary = "The amount a function varies on a set or interval."
aliases = ["oscillation"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/oscillation.md"
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **oscillation** of a bounded function \(f\) on a nonempty set \(A\subseteq\mathbb R\) is
\[
\operatorname{osc}(f;A)=\sup\{|f(x)-f(y)|:x,y\in A\}.
\]
Equivalently,
\[
\operatorname{osc}(f;A)=\sup_{x\in A}f(x)-\inf_{x\in A}f(x).
\]

## Remarks

Oscillation is used in the [[real-analysis/oscillation-criterion|oscillation criterion]] for [[real-analysis/riemann-integrable-function|Riemann integrability]]. A point is a [[real-analysis/discontinuity-point|discontinuity point]] exactly when the oscillation on its shrinking neighborhoods does not tend to \(0\).

## Examples

- For \(f(x)=x\) on \([0,1]\), one has \(\operatorname{osc}(f;[0,1])=1\).
- If \(f\) is the indicator function of \(\mathbb Q\cap[a,b]\), then \(\operatorname{osc}(f;I)=1\) on every nontrivial subinterval \(I\subseteq[a,b]\).
