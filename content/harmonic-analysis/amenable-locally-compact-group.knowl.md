+++
id = "harmonic-analysis/amenable-locally-compact-group"
title = "Amenable locally compact group"
kind = "definition"
summary = "A locally compact group admitting a normalized positive mean invariant under left translation."
aliases = ["amenable group", "group amenability"]
domains = ["harmonic-analysis", "functional-analysis", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/invariant-mean", "harmonic-analysis/haar-measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A [[topology/locally-compact-group|locally compact group]] \(G\) is **amenable** if there exists a left [[harmonic-analysis/invariant-mean|invariant mean]] on \(L^\infty(G)\). Concretely, this is a linear functional
\[
M:L^\infty(G)\longrightarrow\mathbb C
\]
that is positive, satisfies \(M(1)=1\), and obeys
\[
M(L_gf)=M(f)
\qquad\text{for all }g\in G,
\]
where \(L_gf(x)=f(g^{-1}x)\). Here \(L^\infty(G)\) is formed using any left [[harmonic-analysis/haar-measure|Haar measure]]; its measure class is independent of the normalization. Amenability says that invariant averaging exists even when Haar measure cannot be normalized to have finite total mass.

## Equivalent viewpoints

Reiter’s condition \(P_1\) is equivalent to amenability: there is a net of nonnegative functions \(\varphi_i\in L^1(G)\) with \(\lVert\varphi_i\rVert_1=1\) such that
\[
\lVert L_g\varphi_i-\varphi_i\rVert_1\longrightarrow 0
\]
uniformly for \(g\) in compact subsets of \(G\). Another equivalent condition is the fixed-point property: every continuous affine action of \(G\) on a compact convex subset of a [[functional-analysis/locally-convex-space|locally convex space]] has a fixed point. These forms connect averaging, approximation, and dynamics.

## Examples and permanence

Compact groups are amenable because normalized Haar integration is an invariant mean. Locally compact [[algebra-groups/abelian-group|abelian groups]] and solvable locally compact groups are amenable. Closed subgroups, quotients, extensions, and directed unions preserve amenability under the standard locally compact hypotheses. The discrete [[algebra-groups/free-group|free group]] on two generators is the basic non-amenable example.

## Operator-algebraic significance

Amenability can also be detected by [[harmonic-analysis/weak-containment-unitary-representations|weak containment]] of the trivial representation in the [[harmonic-analysis/regular-representations-locally-compact-group|regular representation]]. For group operator algebras, it is equivalent to injectivity of the canonical map from the full to the reduced group \(C^*\)-algebra; this equivalence is isolated in [[operator-algebras/amenability-full-reduced-equivalence|amenability and equality of full and reduced group \(C^*\)-algebras]].

## References

1. Alan L. T. Paterson, *Amenability*, Mathematical Surveys and Monographs 29, American Mathematical Society, 1988. [AMS DOI record](https://doi.org/10.1090/surv/029). Relevant: invariant means and amenability of locally compact groups.
2. Frederick P. Greenleaf, *Invariant Means on Topological Groups and Their Applications*, Van Nostrand Mathematical Studies 16, 1969. [Google Books record](https://books.google.com/books/about/Invariant_Means_on_Topological_Groups_an.html?id=JdwpAQAAMAAJ). Relevant: invariant means on locally compact groups and their applications.
