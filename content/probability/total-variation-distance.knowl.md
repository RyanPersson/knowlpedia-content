+++
id = "probability/total-variation-distance"
title = "Total variation distance"
kind = "knowl"
summary = "A distance between two probability distributions defined by the largest possible difference they assign to the same event."
aliases = ["total-variation-distance", "Total variation distance"]
domains = ["probability"]
prerequisites = ["measure-theory/measurable-set"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "probability/total-variation-distance.md"
+++

A **total variation distance** between probability measures \(P\) and \(Q\) on the same measurable space \((\Omega,\mathcal F)\) is
\[
d_{\mathrm{TV}}(P,Q)\;=\;\sup_{A\in\mathcal F}\,\bigl|P(A)-Q(A)\bigr|
\]
where the supremum ranges over [[measure-theory/measurable-set|measurable sets]] \(A\).

If \(P,Q\ll\mu\) with densities \(p=dP/d\mu\) and \(q=dQ/d\mu\), then
\[
d_{\mathrm{TV}}(P,Q)=\frac12\int_\Omega |p-q|\,d\mu.
\]

## Examples

- For Bernoulli laws with parameters \(p\) and \(q\), \(d_{\mathrm{TV}}(P,Q)=|p-q|\).
- For probability mass functions \((p_i)\) and \((q_i)\) on a finite set,
  \[
  d_{\mathrm{TV}}(P,Q)=\frac12\sum_i|p_i-q_i|.
  \]
