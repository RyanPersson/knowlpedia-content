+++
id = "harmonic-analysis/periodization-of-compactly-supported-function"
title = "Periodization of a compactly supported smooth function"
kind = "definition"
summary = "Summing lattice translates creates a smooth periodic function."
aliases = ["lattice periodization"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/periodic-function", "analysis/locally-finite-smooth-sum", "linear-algebra/euclidean-lattice", "topology/flat-torus", "functional-analysis/test-function-space", "discrete-structures/lattice-zd"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(f\in C_c^\infty(\mathbb R^n)\), its **integer-lattice periodization** is
\[
(\mathcal Pf)(x)=\sum_{k\in\mathbb Z^n}f(x+k).
\]
The sum is locally finite, hence smooth, and it is [[real-analysis/periodic-function|periodic]] under integer translations. It therefore defines a smooth function on \(\mathbb R^n/\mathbb Z^n\).

## Differentiation and separated copies

A compact set meets only finitely many translates of the support, so every derivative commutes with the sum. If \(\operatorname{supp}f\) is a compact subset of the interior of a unit fundamental cube, the translated supports are disjoint with a positive gap. Then at most one summand is nonzero at each point. Without this separation, linear operations still commute with periodization, but nonlinear products can contain cross terms from different copies.
