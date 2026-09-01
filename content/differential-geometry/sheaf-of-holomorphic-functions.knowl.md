+++
id = "differential-geometry/sheaf-of-holomorphic-functions"
title = "Sheaf of holomorphic functions"
kind = "definition"
summary = "The sheaf assigning to each open subset of a complex manifold its algebra of holomorphic functions."
aliases = ["structure sheaf of a complex manifold", "holomorphic structure sheaf"]
domains = ["differential-geometry", "complex-analysis"]
prerequisites = ["differential-geometry/complex-manifold", "algebraic-geometry-foundations/sheaf", "algebraic-geometry-foundations/locally-ringed-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. Its **sheaf of holomorphic functions**, denoted \(\mathcal O_X\), assigns to every open set \(U\subseteq X\) the commutative unital complex algebra
\[
\mathcal O_X(U)=\{f:U\to\mathbb C\mid f\text{ is holomorphic}\},
\]
with restriction maps given by restricting functions to smaller open sets. Holomorphic functions that agree on overlaps glue uniquely, and holomorphicity is local, so this assignment satisfies the [[algebraic-geometry-foundations/sheaf|sheaf]] axioms. The pair \((X,\mathcal O_X)\) is the complex manifold viewed as a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]].

## Stalks and local coordinates

The [[algebraic-geometry-foundations/stalk|stalk]] \(\mathcal O_{X,x}\) consists of germs of holomorphic functions near \(x\). It is a [[algebra-commutative/local-ring|local \(\mathbb C\)-algebra]] whose unique [[algebra-rings/maximal-ideal|maximal ideal]] consists of germs vanishing at \(x\); evaluation at \(x\) identifies the [[algebra-commutative/residue-field|residue field]] with \(\mathbb C\). A [[differential-geometry/complex-coordinate-chart|holomorphic chart]] near \(x\) identifies this stalk with the algebra of germs at the origin of convergent [[real-analysis/power-series|power series]] in \(\dim_{\mathbb C}X\) variables. This identification depends on the chosen chart.

## Functoriality

A [[differential-geometry/holomorphic-map|holomorphic map]] \(F:X\to Y\) pulls local holomorphic functions on \(Y\) back by composition: \(h\mapsto h\circ F\). On stalks this gives local homomorphisms
\[
\mathcal O_{Y,F(x)}\longrightarrow\mathcal O_{X,x}.
\]
Conversely, the compatibility of a [[topology/continuous-map|continuous map]] with these structure sheaves is an intrinsic way to formulate holomorphicity. This ringed-space viewpoint makes local analytic equations, [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundles]], and analytic subspaces accessible without fixing coordinates.

## Conventions and scope

**Warning.** The phrase “[[algebraic-geometry-foundations/structure-sheaf|structure sheaf]]” depends on the geometric category. For a complex manifold it means holomorphic, not merely smooth or continuous, complex-valued functions. The sections over an open set are actual functions on that set, while elements of a stalk are [[shared-foundations/equivalence-class|equivalence classes]] of functions defined only near one point.

## References

1. Robert C. Gunning and Hugo Rossi, *Analytic Functions of Several Complex Variables*, Prentice-Hall, 1965; AMS Chelsea reprint, 2009. [Publisher record](https://doi.org/10.1090/chel/368). Relevant: Chapter I, holomorphic functions, germs, and local rings.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Universitext, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: Chapter 1, complex manifolds and their structure sheaves.
