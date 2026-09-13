+++
id = "partial-differential-equations/poisson-equation"
title = "Poisson equation"
kind = "definition"
summary = "A Laplacian equation with a prescribed source."
aliases = ["inhomogeneous Laplace equation"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/laplacian", "partial-differential-equations/partial-differential-equation", "functional-analysis/distributional-derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **Poisson equation**, with the sign convention used here, is
\[
-\Delta u=f
\]
on a specified open set, where \(\Delta\) is the [[real-analysis/laplacian|Laplacian]] and \(f\) is prescribed. It may be interpreted classically or in distributions, with the solution class stated separately.

## Uniqueness and conventions

The difference of two solutions with the same source is harmonic. Boundary conditions, decay, a norm class, or a normalization are therefore needed to select a unique solution. Some authors instead call \(\Delta u=f\) the Poisson equation; their fundamental solution has the opposite sign.
