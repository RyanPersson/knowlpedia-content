+++
id = "topology/nested-interval-theorem"
title = "Nested interval theorem"
kind = "theorem"
summary = "A nested sequence of nonempty bounded closed intervals in the real line has nonempty intersection."
aliases = ["nested-interval-theorem", "Nested interval theorem"]
domains = ["topology"]
prerequisites = ["real-analysis/interval", "real-analysis/supremum", "real-analysis/infimum"]
dependency_review_count = 1
legacy_source_path = "topology/nested-interval-theorem.md"
+++

**Nested interval theorem:** Let
\[
I_n=[a_n,b_n]\subseteq\mathbb R
\]
be a sequence of nonempty bounded closed [[real-analysis/interval|intervals]]
such that \(I_{n+1}\subseteq I_n\) for all \(n\). Then
\[
\bigcap_{n\in\mathbb N}I_n\neq\varnothing.
\]

More precisely,
\[
\bigcap_{n\in\mathbb N}I_n
=\left[\sup_n a_n,\inf_n b_n\right],
\]
using [[real-analysis/supremum|supremum]] and
[[real-analysis/infimum|infimum]]. If additionally \(b_n-a_n\to 0\), then
the intersection consists of a single point.

## Why boundedness matters

Closedness and nesting alone do not suffice for unbounded intervals: the
sequence \(I_n=[n,\infty)\) has empty intersection. Boundedness makes every
\(I_n\) a compact subset of \(\mathbb R\), so the nonempty intersection
conclusion follows from compactness and the finite intersection property.
The singleton conclusion when \(b_n-a_n\to0\) is the interval case of the
[[topology/cantor-intersection-theorem|Cantor intersection theorem]].
