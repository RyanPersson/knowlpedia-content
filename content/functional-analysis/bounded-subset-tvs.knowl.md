+++
id = "functional-analysis/bounded-subset-tvs"
title = "Bounded subset of a topological vector space"
kind = "definition"
summary = "A subset that is eventually contained in every sufficiently large scalar multiple of each zero-neighborhood."
aliases = ["von Neumann bounded set", "TVS-bounded set"]
domains = ["functional-analysis", "topology"]
section_mode = "progressive"
+++

Let \(X\) be a [[functional-analysis/topological-vector-space|topological vector space]] over \(\mathbb R\) or \(\mathbb C\). A subset \(B\subseteq X\) is **bounded** if every [[topology/neighborhood|neighborhood]] \(U\) of \(0\) [[convex-analysis/balanced-and-absorbing-sets|absorbs]] \(B\): there is \(r>0\) such that
\[
B\subseteq tU
\]
for every scalar \(t\) with \(\lvert t\rvert\geq r\). Equivalently, for every net of nonzero scalars \(t_i\) with \(\lvert t_i\rvert\to\infty\), the rescaled sets \(t_i^{-1}B\) eventually lie in each zero-neighborhood. This is also called **von Neumann boundedness**. It depends on the vector-space topology and need not arise from any metric or norm.

## Comparison with metric boundedness

In a [[linear-algebra/normed-vector-space|normed vector space]], this definition is equivalent to \(\sup_{x\in B}\lVert x\rVert<\infty\): apply the definition to the open unit ball in one direction, and use balls as a zero-neighborhood basis in the other. A general topological vector space may have no distinguished norm, so a statement about finite diameter would not be intrinsic.

## Seminorm criterion

If \(X\) is [[functional-analysis/locally-convex-space|locally convex]], then \(B\) is bounded exactly when
\[
\sup_{x\in B}p(x)<\infty
\]
for every continuous [[convex-analysis/seminorm|seminorm]] \(p\) on \(X\). This criterion turns an apparently topological condition into a family of scalar estimates. It is particularly useful for function spaces whose topologies are specified by many seminorms.

## Stability properties

Finite subsets, [[topology/convergent-sequence|convergent sequences]] together with their limits, and compact subsets are bounded. Finite unions, sums, scalar multiples, and subsets of bounded sets remain bounded. Every [[functional-analysis/continuous-linear-map|continuous linear map]] sends bounded sets to bounded sets. The converse implication does not characterize continuity without extra hypotheses on the source space.

## References

1. Nicolas Bourbaki, *Topological Vector Spaces: Chapters 1–5*, Springer, 2003. [Springer DOI record](https://doi.org/10.1007/978-3-642-61715-7). Relevant: Chapters I–III.
2. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapters I–II.
