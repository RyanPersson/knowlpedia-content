+++
id = "functional-analysis/lf-space"
title = "LF-space"
kind = "definition"
summary = "A Hausdorff locally convex inductive limit of a countable sequence of Fréchet spaces."
aliases = ["countable inductive limit of Fréchet spaces"]
domains = ["functional-analysis"]
prerequisites = ["functional-analysis/locally-convex-space", "functional-analysis/inductive-limit-locally-convex-spaces", "functional-analysis/frechet-space", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **LF-space** is a Hausdorff [[functional-analysis/locally-convex-space|locally convex space]] \(E\) presented as a countable [[functional-analysis/inductive-limit-locally-convex-spaces|locally convex inductive limit]]
\[
E=\varinjlim_{n}E_n,
\]
where every \(E_n\) is a [[functional-analysis/frechet-space|Fréchet space]] and the bonding maps \(E_n\to E_{n+1}\) are continuous [[linear-algebra/linear-map|linear maps]]. When the bonding maps are injective, one usually identifies the stages with an increasing union \(E=\bigcup_n E_n\). The presentation is **strict** if each inclusion gives \(E_n\) the topology induced from \(E_{n+1}\) and has closed image.

## Universal mapping property

A linear map \(T:E\to F\) into a locally convex space is continuous exactly when every composite \(T|_{E_n}:E_n\to F\) is continuous. This is the defining final-topology property of the locally convex inductive limit. It makes stagewise constructions effective even when \(E\) is not metrizable.

## Bounded sets and examples

For a strict LF-space, every bounded subset of \(E\) is contained in some stage \(E_n\) and is bounded there. The basic example is the [[functional-analysis/test-function-space|test-function space]] \(\mathcal D(\Omega)=C_c^\infty(\Omega)\), obtained from Fréchet spaces of smooth functions supported in successive compact subsets of \(\Omega\). Countable locally convex direct sums of Fréchet spaces give further LF-spaces.

## Conventions and properties

LF-spaces are [[functional-analysis/barreled-space|barreled]] and [[functional-analysis/bornological-space|bornological]]. Strict LF-spaces are complete, and their stagewise description gives especially transparent bounded-set behavior. Terminology varies: some authors reserve **LF-space** for strict inductive limits with injective bonding maps, while others use it for arbitrary Hausdorff countable inductive limits of Fréchet spaces. The broader convention is used here, so strictness must be stated when a theorem needs it.

## References

1. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967; Dover reprint, 2006. [Dover publisher record](https://store.doverpublications.com/products/9780486453521). Relevant: Chapters 13–14 on inductive limits and spaces of test functions.
2. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter II on locally convex inductive limits and LF-spaces.
