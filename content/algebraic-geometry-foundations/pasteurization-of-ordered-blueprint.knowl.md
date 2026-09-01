+++
id = "algebraic-geometry-foundations/pasteurization-of-ordered-blueprint"
title = "Unique-weak-inverse reflection of an ordered blueprint"
kind = "construction"
summary = "The universal map from an ordered blueprint to one with unique weak inverses."
aliases = ["pasteurization of an ordered blueprint", "pasteurization functor", "unique weak inverse reflection"]
domains = ["algebraic-geometry-foundations", "algebra-hyperstructures"]
prerequisites = ["algebraic-geometry-foundations/ordered-blueprint", "algebraic-geometry-foundations/ordered-blueprint-with-unique-weak-inverses"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For an [[algebraic-geometry-foundations/ordered-blueprint|ordered blueprint]] \(B\), its **unique-weak-inverse reflection** is an ordered blueprint \(B^\pm\) with unique weak inverses together with a morphism
\[
\eta_B:B\longrightarrow B^\pm
\]
such that every morphism \(B\to C\) into an [[algebraic-geometry-foundations/ordered-blueprint-with-unique-weak-inverses|ordered blueprint with unique weak inverses]] factors uniquely through \(\eta_B\).

In categorical terms, \(B\mapsto B^\pm\) is left adjoint to the inclusion
\[
\operatorname{OBlpr}^{\pm}\hookrightarrow\operatorname{OBlpr}.
\]
Thus \(\operatorname{OBlpr}^{\pm}\) is a reflective full subcategory.

## Construction

One first tensors with \(\mathbb F_1^\pm\) to adjoin weak inverses. One then identifies any two elements that serve as weak inverses of the same element. Schematically,
\[
B^\pm=
\bigl(B\otimes_{\mathbb F_1}\mathbb F_1^\pm\bigr)/\!\sim,
\]
where \(a\sim a'\) when some \(b\) satisfies both \(0\leq a+b\) and \(0\leq a'+b\). The resulting quotient enforces uniqueness.

## Terminology and caution

This reflector was historically called **pasteurization**. The canonical ID retains that established name, but the title uses current terminology. The reflection need not embed \(B\): its unit \(\eta_B\) may identify elements. It is also not a passage from a semiring to a ring; weak inverses are order-theoretic.

## References
Oliver Lorscheid, [*Blueprints and tropical scheme theory*, Definition 5.6.30 and Exercise 5.6.31](https://lorscheid.org/notes/2018-Blueprints/versions/lecturenotes180521.pdf).

