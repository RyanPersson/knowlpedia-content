+++
id = "topology/annulus"
title = "Euclidean annulus"
kind = "definition"
summary = "The region between two concentric Euclidean spheres."
aliases = ["spherical shell", "annular region"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-norm", "real-analysis/interval"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a center \(a\in\mathbb R^n\) and radii \(0<r<R\), the **open annulus** is
\[
A(a;r,R)=\{x\in\mathbb R^n:r<|x-a|<R\}.
\]
Replacing one or both inequalities by non-strict ones gives half-open or closed versions. In two dimensions this is a ring-shaped region; in higher dimensions “spherical shell” is also used.

## Cylindrical and dyadic versions

A cylindrical annular region in \(\mathbb R^3\) restricts \(\sqrt{x^2+y^2}\) between two positive radii, possibly also restricting \(z\). It stays away from the coordinate axis. A [[analysis/dyadic-annulus|dyadic annulus]] has outer radius twice its inner radius and is useful for sorting estimates by scale.
