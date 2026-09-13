+++
id = "fluid-dynamics/vortex-line"
title = "Vortex line"
kind = "definition"
summary = "A curve tangent to the vorticity vector field at a fixed time."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/vorticity", "differential-equations/ordinary-differential-equation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

At a fixed time \(t\), a **vortex line** is a curve tangent to the [[fluid-dynamics/vorticity|vorticity field]]. On a region where \(\omega(t,x)\ne0\), one parametrization solves
\[
\frac{d\gamma}{ds}=\omega(t,\gamma(s)).
\]
Reparametrizing by a nonzero scalar factor gives the same unparametrized tangent curves.

## Trajectories and structures

The time \(t\) is held fixed in this definition. A vortex line is therefore different from a fluid particle trajectory, whose time derivative is the velocity \(u\). Vortex tubes and other vortex structures are organized using vorticity geometry, but the word “vortex” by itself does not select a universal quantitative criterion.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
