+++
id = "functional-analysis/inductive-limit-locally-convex-spaces"
title = "Inductive limit of locally convex spaces"
kind = "definition"
summary = "The algebraic direct limit equipped with the finest locally convex topology making its structure maps continuous."
aliases = ["direct limit topology", "locally convex inductive limit"]
domains = ["functional-analysis"]
prerequisites = ["functional-analysis/locally-convex-space", "functional-analysis/continuous-linear-map", "linear-algebra/linear-map", "topology/topological-space", "functional-analysis/topological-vector-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((E_i,\phi_{ji})\) be a directed system of [[functional-analysis/locally-convex-space|locally convex spaces]] and [[functional-analysis/continuous-linear-map|continuous linear maps]], and let \(E=\varinjlim E_i\) be its algebraic direct limit with canonical [[linear-algebra/linear-map|linear maps]] \(\iota_i:E_i\to E\). The **locally convex inductive-limit topology** on \(E\) is the finest locally convex vector topology for which every \(\iota_i\) is continuous. The resulting locally convex space is denoted
\[
\varinjlim E_i
\quad\text{or}\quad
\operatorname{ind\,lim}_i E_i.
\]
This is a categorical final construction within locally convex spaces. It need not equal the ordinary final topology in [[topology/topological-space|topological spaces]], because that topology need not make \(E\) a locally convex [[functional-analysis/topological-vector-space|topological vector space]].

## Universal property

For every locally convex space \(F\), a linear map \(T:E\to F\) is continuous exactly when each composite
\[
T\circ\iota_i:E_i\to F
\]
is continuous. This property characterizes the inductive limit up to canonical topological isomorphism and is often the most efficient way to prove continuity of a linear map defined on the limit.

## Increasing sequences

A common case is an increasing sequence
\[
E_1\subseteq E_2\subseteq\cdots,\qquad E=\bigcup_{n\geq1}E_n,
\]
with continuous inclusions. If every \(E_n\) is Fréchet, the inductive limit is called an **LF-space**. [[functional-analysis/test-function-space|Compactly supported smooth functions]] are obtained in this way by taking smooth functions supported in a fixed [[topology/compact-set|compact set]] and then enlarging the compact set.

## Hausdorffness and regularity

Some authors require locally convex spaces to be Hausdorff. In that convention, a non-Hausdorff locally convex inductive limit must be divided by the closure of \(\{0\}\) to obtain the categorical Hausdorff limit. Completeness, bounded-set behavior, and the compatibility of [[topology/subspace-topology|subspace topologies]] do not follow formally from the definition; adjectives such as **strict**, **regular**, and **complete** record extra hypotheses.

## References

1. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Elsevier book record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: Chapters 13–14.
2. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter II.
