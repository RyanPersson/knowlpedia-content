+++
id = "fluid-dynamics/particle-trajectory"
title = "Particle trajectory of a velocity field"
kind = "definition"
summary = "A curve whose tangent velocity equals the fluid velocity at its current position."
aliases = ["Lagrangian trajectory", "fluid flow map"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "differential-equations/initial-value-problem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **particle trajectory** for a velocity field \(u\), starting at \(a\) at time \(s\), solves
\[
\frac{d}{dt}X(t;s,a)=u(t,X(t;s,a)),
\qquad X(s;s,a)=a.
\]
Where these [[differential-equations/initial-value-problem|initial-value problems]] have unique solutions, \(a\mapsto X(t;s,a)\) is the **flow map** from time \(s\) to time \(t\).

## Local existence

Continuity in time and local Lipschitz continuity in position give local existence and uniqueness by the [[differential-equations/picard-lindelof-theorem|Picard–Lindelöf theorem]]. The trajectory is followed only while it remains in the region and time interval where the field is defined.

## Lagrangian description

The coordinate \(a\) labels a particle. A field sampled along that trajectory is \(q(t,X(t;s,a))\); its time derivative is the [[fluid-dynamics/material-derivative|material derivative]] of \(q\).

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
