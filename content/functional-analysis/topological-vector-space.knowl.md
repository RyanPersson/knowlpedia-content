+++
id = "functional-analysis/topological-vector-space"
title = "Topological vector space"
kind = "definition"
summary = "A vector space with a Hausdorff topology for which addition and scalar multiplication are continuous."
aliases = ["TVS", "linear topological space"]
domains = ["functional-analysis", "topology"]
section_mode = "progressive"
+++

Let \(\mathbb F=\mathbb R\) or \(\mathbb C\). A **topological vector space over \(\mathbb F\)** is a [[linear-algebra/vector-space|vector space]] \(V\) equipped with a [[topology/topological-space|Hausdorff topology]] such that the maps
\[
V\times V\longrightarrow V,\quad(x,y)\longmapsto x+y,
\qquad
\mathbb F\times V\longrightarrow V,\quad(a,x)\longmapsto ax
\]
are [[topology/continuous-map|continuous]] for the [[topology/product-topology|product topologies]]. Consequently, translations \(x\mapsto x+v\) and multiplication by any nonzero scalar are homeomorphisms. All local topological information can therefore be transported from a [[topology/neighborhood|neighborhood]] of \(0\) to any point.

## Neighborhood structure

Continuity of addition implies that for every neighborhood \(U\) of \(0\), there is a neighborhood \(W\) of \(0\) with \(W+W\subseteq U\). Continuity of scalar multiplication supplies balanced neighborhoods after shrinking. These properties define a translation-invariant uniform structure, so notions such as Cauchy nets and completeness make sense even when no metric or norm is specified.

## Linear maps and duality

A linear map between topological vector spaces is continuous everywhere exactly when it is continuous at \(0\). The [[functional-analysis/topological-dual|continuous dual]] \(V'\) consists of all continuous linear maps \(V\to\mathbb F\); it can be much smaller than the algebraic dual and can even fail to separate points without additional hypotheses. [[functional-analysis/locally-convex-space|Locally convex spaces]] impose enough convex neighborhoods to bring separation theorems and rich duality into play [Schaefer–Wolff, Chapters II–IV](https://doi.org/10.1007/978-1-4612-1468-7).

## Examples and conventions

Every [[linear-algebra/normed-vector-space|normed vector space]] is a topological vector space for its norm topology. Products of topological vector spaces, spaces of smooth test functions, and spaces of distributions provide important examples whose natural topologies need not come from a single norm. A [[linear-algebra/banach-space|Banach space]] is the special case of a complete normed vector space.

**Warning.** Some authors do not require Hausdorffness in the definition. It is required here. A topological vector space is not automatically locally convex, metrizable, normable, or complete.

## References

1. H. H. Schaefer and M. P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapters II–IV on topological vector spaces, locally convex spaces, linear mappings, and duality.
