+++
id = "topology/hausdorff-distance"
title = "Hausdorff distance"
kind = "definition"
summary = "The maximum discrepancy between two nonempty compact subsets of a metric space."
aliases = ["Hausdorff metric", "Hausdorff convergence"]
domains = ["topology", "metric-geometry", "convex-analysis"]
section_mode = "progressive"
prerequisites = ["topology/metric-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For nonempty compact subsets \(A,B\) of a
[[topology/metric-space|metric space]] \((X,d)\), their **Hausdorff distance**
is
\[
d_H(A,B)=\max\left\{
\sup_{a\in A}d(a,B),\qquad
\sup_{b\in B}d(b,A)
\right\},
\]
where \(d(x,C)=\inf_{c\in C}d(x,c)\).

## Neighborhood form

Equivalently,
\[
d_H(A,B)=\inf\{\varepsilon>0:
A\subseteq B_\varepsilon\text{ and }B\subseteq A_\varepsilon\}.
\]
On the nonempty compact subsets of \(X\), this is a genuine metric. For more
general closed unbounded subsets it may be infinite.

## Convex bodies

On [[convex-analysis/convex-body|convex bodies]] in a finite-dimensional
[[linear-algebra/vector-space|vector space]], the topology induced by \(d_H\)
does not depend on the chosen [[linear-algebra/euclidean-norm|Euclidean norm]].
Under a fixed norm it agrees with
[[real-analysis/uniform-convergence|uniform convergence]] of
[[convex-analysis/support-function|support functions]] on the dual unit
sphere.

## References

1. Dmitri Burago, Yuri Burago, and Sergei Ivanov, *A Course in Metric Geometry*, AMS, 2001. [DOI record](https://doi.org/10.1090/gsm/033). Relevant: §7.3.
2. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014. [DOI record](https://doi.org/10.1017/CBO9781139003858). Relevant: §1.8.
