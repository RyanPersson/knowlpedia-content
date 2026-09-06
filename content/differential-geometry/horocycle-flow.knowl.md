+++
id = "differential-geometry/horocycle-flow"
title = "Horocycle flow"
kind = "definition"
summary = "The stable or unstable unipotent flow on the unit tangent bundle of a hyperbolic surface."
aliases = ["stable horocycle flow", "unstable horocycle flow"]
domains = ["differential-geometry", "dynamical-systems", "quantum-chaos"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/tangent-bundle", "lie-groups/right-translation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

On an oriented hyperbolic surface \(M=\Gamma\backslash\mathbb H^2\), identify
the unit [[fiber-bundles/tangent-bundle|tangent bundle]] with \(\Gamma\backslash PSL(2,\mathbb R)\). A
**horocycle flow** is [[lie-groups/right-translation|right translation]] by one of the unipotent subgroups
\[
n_s^+=\begin{pmatrix}1&s\\0&1\end{pmatrix},
\qquad
n_s^-=\begin{pmatrix}1&0\\s&1\end{pmatrix}.
\]
The two choices give the unstable and stable horocycle flows.

## Geometric picture

Projected orbits trace horocycles: curves orthogonal to all geodesics
converging to the same point on the ideal boundary. The [[differential-geometry/geodesic-flow|geodesic flow]] expands
one horocycle direction and contracts the other.

## Compact quotients

For a [[mathematical-physics/compact-hyperbolic-surface|compact hyperbolic surface]], each horocycle flow is
[[analysis/unique-ergodicity|uniquely ergodic]]. This recurrence forces the
endpoint set of geodesics avoiding a fixed nonempty open set to have holes at
all relevant scales.

## References

1. Gustav A. Hedlund, “Fuchsian groups and transitive horocycles,” *Duke Mathematical Journal* 2 (1936), 530–542. [DOI record](https://doi.org/10.1215/S0012-7094-36-00246-6).
