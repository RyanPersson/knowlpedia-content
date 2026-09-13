+++
id = "partial-differential-equations/conservation-law"
title = "Conservation law in divergence form"
kind = "definition"
summary = "An evolution equation equating the change of a density plus the divergence of its flux to a source."
aliases = ["conservative form", "divergence form conservation law"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/divergence", "real-analysis/partial-derivative", "real-analysis/euclidean-vector-field"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A scalar **conservation law with source** has the form
\[
\partial_tq+\nabla\cdot J=s,
\]
where \(q\) is a density, \(J\) its spatial flux, and \(s\) a source. It is homogeneous when \(s=0\). The spatial [[real-analysis/divergence|divergence]] gives a **conservative** or **divergence form** of the evolution equation.

## Integral meaning

For a fixed bounded region \(\Omega\) with smooth boundary, sufficient regularity and the divergence theorem give
\[
\frac{d}{dt}\int_\Omega q\,dx
=-\int_{\partial\Omega}J\cdot n\,dS+\int_\Omega s\,dx,
\]
where \(n\) is the outward unit normal. The negative sign accounts for outward flux reducing the amount inside.

## Systems

For vector-valued densities, each component has its own flux. These fluxes form a matrix, and the system uses its [[real-analysis/divergence-of-tensor|row divergence]].
