+++
id = "fluid-dynamics/velocity-field"
title = "Fluid velocity field"
kind = "definition"
summary = "The vector assigning the instantaneous fluid velocity to each point of space and time."
aliases = ["Eulerian velocity field", "velocity in fluid mechanics"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/euclidean-vector-field", "shared-foundations/cartesian-product", "real-analysis/interval"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **fluid velocity field** on a spatial domain \(\Omega\subseteq\mathbb R^d\) and time interval \(I\) is a map
\[
u:I\times\Omega\to\mathbb R^d.
\]
The vector \(u(t,x)\) is the instantaneous velocity of fluid at the spatial point \(x\) and time \(t\). This is the Eulerian description: the coordinate \(x\) labels a location, rather than a fixed fluid particle.

## Regularity and components

Regularity is an additional hypothesis; one may study smooth, continuous, or measurable velocity fields. The scalar components \(u_i\) are taken in a specified basis. A time slice \(u(t,\cdot)\) is a [[real-analysis/euclidean-vector-field|Euclidean vector field]].

Particle motion is described by the [[fluid-dynamics/particle-trajectory|trajectory equation]] \(X'(t)=u(t,X(t))\).

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
