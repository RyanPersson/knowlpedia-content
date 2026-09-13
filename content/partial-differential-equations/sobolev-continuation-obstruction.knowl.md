+++
id = "partial-differential-equations/sobolev-continuation-obstruction"
title = "Supremum growth obstructs continuous Sobolev continuation"
kind = "theorem"
summary = "An embedding into bounded functions turns unbounded supremum norm into failure of continuous Hs extension."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/finite-time-blowup", "functional-analysis/sobolev-embedding-bounded-derivatives", "topology/continuous-map", "topology/compact-set", "functional-analysis/fourier-sobolev-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Suppose \(u\in C([0,T);H^s(\mathbb R^n))\), \(T<\infty\), and \(s>n/2\). If
\[
\limsup_{t\uparrow T}\|u(t)\|_\infty=\infty,
\]
then \(u\) cannot extend continuously in \(H^s\) to an interval containing \([0,T]\). This is a direct consequence of the [[functional-analysis/sobolev-embedding-bounded-derivatives|Sobolev embedding into bounded functions]].

## Proof and scope

A continuous map from the compact time interval \([0,T]\) into \(H^s\) has bounded \(H^s\) norm. The embedding then gives a uniform \(L^\infty\) bound, contradicting the displayed growth. This establishes an obstruction to extension. It does not prove that every finite maximal lifespan forces supremum growth; that converse needs an actual continuation theorem for the equation and solution class.
