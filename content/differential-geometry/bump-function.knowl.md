+++
id = "differential-geometry/bump-function"
title = "Bump function"
kind = "definition"
summary = "A smooth function with compact support, often chosen to equal one on a prescribed closed set."
aliases = ["smooth bump function", "smooth cutoff function"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-map", "topology/compact-set", "topology/closed-set", "topology/neighborhood"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. A **bump function** is a [[fiber-bundles/smooth-map|smooth map]] \(\varphi:M\to\mathbb R\) whose support
\[
\operatorname{supp}\varphi=\overline{\{p\in M:\varphi(p)\ne0\}}
\]
is a [[topology/compact-set|compact set]]. In localized constructions one usually requires more: for a [[topology/closed-set|closed set]] \(A\subseteq M\) and an open set \(U\supseteq A\), a bump function **for \(A\) supported in \(U\)** satisfies \(0\le\varphi\le1\), equals \(1\) on a [[topology/neighborhood|neighborhood]] of \(A\), and has \(\operatorname{supp}\varphi\subseteq U\).

## Existence on smooth manifolds

If \(A\subseteq U\subseteq M\), with \(A\) closed and \(U\) open, and \(A\) is compact, then such a function exists. The proof first constructs Euclidean cutoff functions and then combines local constructions using a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity]].

## Uses and constructions

Bump functions extend locally defined objects, splice constructions without changing them on a chosen region, and build [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]]. If \(s\) is a local section over \(U\) and \(\varphi\) has support contained in \(U\), then \(\varphi s\), extended by zero, is a global smooth section.

## Conventions and non-examples

Some authors use “cutoff function” for the more specific \(0\)-to-\(1\) function adapted to \(A\subseteq U\), and others do not require every cutoff to have compact support. The constant function \(1\) is therefore a bump function precisely when \(M\) is compact. A compactly supported continuous function with a corner is not a smooth bump function.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth functions, bump functions, and partitions of unity.
2. Jet Nestruev, *Smooth Manifolds and Observables*, Springer, 2003. [DOI record](https://doi.org/10.1007/b98871). Relevant: “Cutoff and Other Special Smooth Functions.”
