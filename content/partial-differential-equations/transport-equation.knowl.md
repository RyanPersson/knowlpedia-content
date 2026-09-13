+++
id = "partial-differential-equations/transport-equation"
title = "Transport equation"
kind = "definition"
summary = "An equation prescribing the material derivative of a scalar field along a given velocity."
aliases = ["advection equation"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/material-derivative", "partial-differential-equations/partial-differential-equation", "fluid-dynamics/particle-trajectory"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **transport equation** for a scalar \(a(t,x)\), with prescribed velocity \(b(t,x)\) and source \(g(t,x)\), is
\[
\partial_ta+b\cdot\nabla a=g.
\]
For sufficiently regular fields and a [[fluid-dynamics/particle-trajectory|trajectory]] satisfying \(X'=b(t,X)\), it becomes
\[
\frac{d}{dt}a(t,X(t))=g(t,X(t)).
\]
Thus source-free transport preserves the scalar value along each trajectory.

## Density transport

The conservative density equation is \(\partial_ta+\nabla\cdot(ab)=g\). It equals the displayed transport equation when \(\nabla\cdot b=0\); otherwise it has the additional term \(a\nabla\cdot b\).

Adding \(\nu\Delta a\) on the right gives an advection-diffusion equation. Transport and diffusion then act simultaneously.

## References

- [Lenya Ryzhik, Lecture Notes for Math 256B (2024), Sections 1–3](https://virtualmath1.stanford.edu/~ryzhik/notes-256B-24.pdf).
