+++
id = "topology/homotopy"
title = "Homotopy"
kind = "definition"
summary = "A continuous map on a product with the unit interval that interpolates between two maps."
aliases = ["homotopic", "homotopy of maps"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/continuous-map", "topology/product-topology", "real-analysis/interval"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 1
+++

A **homotopy** from [[topology/continuous-map|continuous maps]] \(f,g:X\to Y\) is a continuous map
\[
H:X\times[0,1]\to Y,\qquad H(x,0)=f(x),\quad H(x,1)=g(x),
\]
where the domain has the [[topology/product-topology|product topology]]. If one exists, \(f\) and \(g\) are **homotopic**, written \(f\simeq g\).

## Fixing a subset

For \(A\subseteq X\), a homotopy relative to \(A\) additionally satisfies \(H(a,t)=f(a)=g(a)\) for every \(a\in A\) and \(t\in[0,1]\). In the [[topology/fundamental-group|fundamental group]], homotopies of paths fix both endpoints.

## Example

For maps into a convex subset of \(\mathbb R^n\), \(H(x,t)=(1-t)f(x)+tg(x)\) is a homotopy.

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, §0 and §1.1. [Author-hosted text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
