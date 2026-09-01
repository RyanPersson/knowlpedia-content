+++
id = "functional-analysis/banach-alaoglu-theorem"
title = "Banach–Alaoglu theorem"
kind = "theorem"
summary = "The closed unit ball of the continuous dual of a normed space is compact in the weak-star topology."
aliases = ["Alaoglu theorem", "weak-star compactness theorem"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/normed-vector-space", "functional-analysis/topological-dual", "functional-analysis/weak-star-topology"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a
[[linear-algebra/normed-vector-space|normed vector space]] over
\(\mathbb R\) or \(\mathbb C\), and let \(X'\) be its
[[functional-analysis/topological-dual|continuous dual]]. The
**Banach–Alaoglu theorem** states that the closed dual unit ball
\[
B_{X'}=\{\varphi\in X':\lVert\varphi\rVert\leq1\}
\]
is compact in the
[[functional-analysis/weak-star-topology|weak-star topology]]
\(\sigma(X',X)\). Completeness of \(X\) is not required. The conclusion is
weak-star compactness; in an infinite-dimensional setting, the same ball is
not compact in its norm topology.

## Proof mechanism

Evaluation embeds \(B_{X'}\) into the product
\[
\prod_{x\in X}\{z:|z|\leq\lVert x\rVert\}.
\]
Each factor is compact, so the product is compact by Tychonoff's theorem. The
linearity and norm inequalities defining the image are closed conditions in
the [[topology/product-topology|product topology]]. The
[[topology/subspace-topology|subspace topology]] induced by this embedding is
exactly \(\sigma(X',X)\), proving compactness.

## Consequences and scope

If \(X\) is separable, the weak-star topology on \(B_{X'}\) is metrizable;
Banach–Alaoglu then supplies sequential compactness as well. Without
separability, compactness need not be detectable by sequences. Applying the
theorem to the bidual, together with the canonical embedding, helps show that
the closed unit ball of a
[[functional-analysis/reflexive-banach-space|reflexive Banach space]] is
weakly compact.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter V, “Weak Topologies.”
2. Walter Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill, 1991. [WorldCat record](https://search.worldcat.org/title/21163277). Relevant: Chapter 3, compactness in dual spaces.
