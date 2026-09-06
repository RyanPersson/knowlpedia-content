+++
id = "topology/boundary"
title = "Boundary"
kind = "knowl"
summary = "The set of points where every neighborhood meets both the set and its complement."
aliases = ["boundary"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "topology/closure", "topology/interior"]
dependency_review_count = 1
legacy_source_path = "topology/boundary.md"
+++

Let \(X\) be a [[topology/topological-space|topological space]] and let \(A\subseteq X\). The **boundary** of \(A\), denoted \(\partial A\), is
\[\partial A := \overline{A}\setminus \operatorname{int}(A).\]

## Equivalent characterizations

Equivalently,
\[\partial A = \overline{A}\cap \overline{X\setminus A}\]

(see [[topology/closure|closure]] and [[topology/interior|interior]]). Equivalently again, \(x\in\partial A\) iff every [[topology/neighborhood|neighborhood]] of \(x\) meets both \(A\) and \(X\setminus A\).

## Remarks

Boundaries isolate the "edge" of a set and play a key role in topology and analysis (e.g., in describing discontinuity sets and in integration theory).

## Examples

- In \(\mathbb{R}\), \(\partial(0,1)=\{0,1\}\).
- In \(\mathbb{R}^2\), the boundary of the open unit disk \(B(0,1)\) is the unit circle \(S(0,1)\).
- If \(A=\mathbb{Q}\subseteq\mathbb{R}\), then \(\partial A=\mathbb{R}\) (every interval meets both \(\mathbb{Q}\) and \(\mathbb{R}\setminus\mathbb{Q}\)).
