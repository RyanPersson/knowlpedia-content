+++
id = "measure-theory/borel-measure"
title = "Borel measure"
kind = "definition"
summary = "A measure defined on the Borel sigma-algebra of a topological space."
aliases = ["Borel measure"]
domains = ["measure-theory", "topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "measure-theory/borel-sigma-algebra", "measure-theory/measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[topology/topological-space|topological space]] and \(\mathcal B(X)\) its [[measure-theory/borel-sigma-algebra|Borel sigma-algebra]]. A **Borel measure** is a [[measure-theory/measure|measure]] \(\mu:\mathcal B(X)\to[0,\infty]\).

## Additional hypotheses

“Borel measure” specifies the measurable sets, not regularity, finiteness, or local finiteness. Those are separate assumptions. A regular locally finite Borel measure on a locally compact Hausdorff space is often called a Radon measure.

## Examples

[[measure-theory/lebesgue-measure|Lebesgue measure]] restricted to Borel subsets of \(\mathbb R^n\) and a Dirac measure \(\delta_x\), defined by \(\delta_x(E)=1\) if \(x\in E\) and \(0\) otherwise, are Borel measures. [[harmonic-analysis/haar-measure|Haar measure]] is a regular Borel measure with the additional translation-invariance property.

## References

1. Gerald B. Folland, *Real Analysis*, 2nd ed., Wiley, 1999. Relevant: Chapter 7, Borel and regular measures.
