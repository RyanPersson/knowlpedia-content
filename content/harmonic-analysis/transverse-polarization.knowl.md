+++
id = "harmonic-analysis/transverse-polarization"
title = "Transverse polarization of a vector wave"
kind = "definition"
summary = "An amplitude lying in the plane perpendicular to the local wavevector."
aliases = ["velocity polarization", "transverse amplitude"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/wave-amplitude", "harmonic-analysis/wavevector", "linear-algebra/orthogonal-complement", "real-analysis/divergence", "linear-algebra/inner-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A vector wave \(ae^{i\kappa\Phi}\) is **transversely polarized** for \(\kappa\ne0\) at a point with \(\nabla\Phi\ne0\) if
\[
\nabla\Phi\cdot a=0.
\]
Its [[harmonic-analysis/wave-amplitude|amplitude]] lies in the plane perpendicular to the phase gradient. For complex amplitudes the dot product with this real normal is extended complex linearly, so both real and imaginary parts are transverse.

## Leading and exact incompressibility

The identity
\[
\nabla\cdot(ae^{i\kappa\Phi})
=e^{i\kappa\Phi}\bigl(\nabla\cdot a+i\kappa\nabla\Phi\cdot a\bigr)
\]
shows that transversality cancels the leading frequency term. Exact divergence freedom additionally requires \(\nabla\cdot a=0\), or a correction that cancels it. For a constant-amplitude plane wave transversality is sufficient.
