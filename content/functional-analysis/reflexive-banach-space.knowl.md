+++
id = "functional-analysis/reflexive-banach-space"
title = "Reflexive Banach space"
kind = "definition"
summary = "A Banach space whose canonical embedding into its continuous bidual is surjective."
aliases = ["reflexive space", "canonical bidual isomorphism"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(X\) be a [[linear-algebra/banach-space|Banach space]] over
\(\mathbb R\) or \(\mathbb C\), let \(X'\) be its
[[functional-analysis/topological-dual|continuous dual]], and let
\(X''=(X')'\). The canonical evaluation map
\[
J_X:X\to X'',\qquad (J_Xx)(\varphi)=\varphi(x),
\]
is a linear isometry. The space \(X\) is **reflexive** if \(J_X\) is
surjective. Equivalently, every continuous linear functional on \(X'\) is
evaluation at a unique vector of \(X\). Reflexivity is therefore a property
of the Banach-space topology, not merely an algebraic identification with a
double dual.

## Equivalent characterizations

A Banach space is reflexive exactly when its closed unit ball is compact for
the [[functional-analysis/weak-topology|weak topology]]. By the
Eberlein–Šmulian theorem, this is also equivalent to weak sequential
compactness of the unit ball. These are theorem-level characterizations, not
parts of the definition.

## Examples and permanence

Every finite-dimensional Banach space and every
[[linear-algebra/hilbert-space|Hilbert space]] is reflexive. For a measure
space, \(L^p\) is reflexive when \(1<p<\infty\); in contrast, \(\ell^1\),
\(c_0\), and infinite-dimensional \(L^1\) spaces are standard nonexamples.
Closed subspaces and Banach-space quotients of a reflexive space are
reflexive. Moreover, \(X\) is reflexive exactly when \(X'\) is reflexive.

## Conventions and scope

Some authors call a
[[functional-analysis/locally-convex-space|locally convex space]] reflexive
when a canonical map into a suitably topologized bidual is an isomorphism.
That broader notion depends on which dual topology is chosen. This knowl uses
the Banach-space convention, where both duals carry their norm topologies and
surjectivity of \(J_X\) is the defining condition.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter V, “Weak Topologies.”
2. Walter Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill, 1991. [WorldCat record](https://search.worldcat.org/title/21163277). Relevant: Chapter 4, reflexivity and weak compactness.
