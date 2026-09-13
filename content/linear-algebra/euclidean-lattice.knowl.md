+++
id = "linear-algebra/euclidean-lattice"
title = "Full-rank Euclidean lattice"
kind = "definition"
summary = "Integer linear combinations of a basis of a Euclidean space."
aliases = ["full-rank lattice", "Euclidean lattice"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-space", "convex-analysis/basis-hamel-basis-and-dimension", "discrete-structures/lattice-zd", "linear-algebra/matrix-inverse", "linear-algebra/operator-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A **full-rank Euclidean lattice** in \(\mathbb R^n\) is a set
\[
\Lambda=B\mathbb Z^n=\{Bm:m\in\mathbb Z^n\},
\]
where the columns of \(B\) form a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] of \(\mathbb R^n\). Thus \(B\) is invertible. The lattice is an additive subgroup and is discrete: \(|Bm|\ge |m|/\|B^{-1}\|\), so its nonzero points have a positive lower bound on their distance from zero.

## Basis choices

Different bases can describe the same lattice. Replacing \(B\) by \(BU\), where \(U\) is an integer matrix with integer inverse, preserves \(\Lambda\). The standard example is [[discrete-structures/lattice-zd|\(\mathbb Z^n\)]]. Here “lattice” refers to a discrete additive set in Euclidean space; an [[shared-foundations/lattice|order-theoretic lattice]] is a different structure.
