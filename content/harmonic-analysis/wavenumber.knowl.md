+++
id = "harmonic-analysis/wavenumber"
title = "Wavenumber"
kind = "definition"
summary = "The magnitude of an angular wavevector, measuring radians of phase change per unit distance."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/wavevector", "linear-algebra/euclidean-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[harmonic-analysis/wavevector|wavevector]] \(k\), the **angular wavenumber** is \(|k|\), its Euclidean length. It measures spatial phase variation in radians per unit distance. In one dimension authors may instead use a signed wavenumber; the convention must be stated.

## Frequency parameters

For \(e^{i\kappa\Phi}\), the local wavenumber is \(|\kappa|\,|\nabla\Phi|\), not merely \(|\kappa|\). If \(\nabla\Phi\) changes along a flow, viscous damping changes even when the carrier parameter \(\kappa\) is fixed.
