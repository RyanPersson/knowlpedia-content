+++
id = "fluid-dynamics/conservative-momentum-equation"
title = "Conservative incompressible momentum equation"
kind = "identity"
summary = "The Navier–Stokes momentum equation written as the divergence of a total momentum flux."
aliases = ["conservative momentum balance"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "fluid-dynamics/momentum-flux", "partial-differential-equations/conservation-law", "real-analysis/divergence-of-tensor", "real-analysis/schwarz-clairaut-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For smooth divergence-free velocity and constant \(\nu\), the [[fluid-dynamics/navier-stokes-equations|Navier–Stokes momentum equation]] is equivalent to
\[
\partial_tu+\nabla\cdot
\bigl(u\otimes u+pI-\nu(\nabla u+(\nabla u)^{\mathsf T})\bigr)=f.
\]
The divergence of a matrix is taken row by row: \((\nabla\cdot J)_i=\sum_j\partial_jJ_{ij}\).

## Verification

The product rule yields
\[
\nabla\cdot(u\otimes u)=(u\cdot\nabla)u+u(\nabla\cdot u),
\]
while equality of mixed derivatives gives
\[
\nabla\cdot(\nabla u+(\nabla u)^{\mathsf T})
=\Delta u+\nabla(\nabla\cdot u).
\]
Both extra terms vanish under incompressibility. Also \(\nabla\cdot(pI)=\nabla p\).

## Simpler equivalent flux

For divergence-free velocity, \(u\otimes u+pI-\nu\nabla u\) has the same divergence as the symmetric-stress flux. The flux tensors differ, but their local momentum equations coincide under this constraint.
