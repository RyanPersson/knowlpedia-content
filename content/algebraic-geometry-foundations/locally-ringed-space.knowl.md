+++
id = "algebraic-geometry-foundations/locally-ringed-space"
title = "Locally ringed space"
kind = "knowl"
summary = "A topological space with a sheaf of rings whose stalks are local rings."
aliases = ["locally-ringed-space", "Locally ringed space"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["topology/topological-space", "algebraic-geometry-foundations/sheaf", "algebraic-geometry-foundations/stalk", "algebra-commutative/local-ring", "algebraic-geometry-foundations/structure-sheaf"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebraic-geometry-foundations/locally-ringed-space.md"
+++

A **locally ringed space** is a pair \((X,\mathcal O_X)\) consisting of a [[topology/topological-space|topological space]] \(X\) and a [[algebraic-geometry-foundations/sheaf|sheaf]] of commutative rings \(\mathcal O_X\) such that every [[algebraic-geometry-foundations/stalk|stalk]] \(\mathcal O_{X,x}\) is a [[algebra-commutative/local-ring|local ring]]. The sheaf \(\mathcal O_X\) is called the [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]].

The unique maximal ideal in \(\mathcal O_{X,x}\) distinguishes functions that vanish at \(x\) from those locally invertible near \(x\). This extra condition makes points and local algebra interact correctly.

## Examples

For example, if \(A\) is a commutative ring, then \((\operatorname{Spec}A,\mathcal O_{\operatorname{Spec}A})\) is locally ringed because the stalk at a prime ideal \(\mathfrak p\) is the local ring \(A_{\mathfrak p}\). Such examples are precisely the [[algebraic-geometry-foundations/affine-scheme|affine schemes]].
