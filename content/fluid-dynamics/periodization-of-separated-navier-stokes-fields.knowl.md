+++
id = "fluid-dynamics/periodization-of-separated-navier-stokes-fields"
title = "Periodization of separated incompressible flows"
kind = "theorem"
summary = "Disjoint translated supports preserve the nonlinear momentum equation under lattice periodization."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/periodization-of-compactly-supported-function", "fluid-dynamics/navier-stokes-equations", "analysis/separated-support-products", "topology/flat-torus"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \((u,p,f)\) be smooth whole-space [[fluid-dynamics/navier-stokes-equations|Navier–Stokes fields]] whose common spatial support lies in one fixed compact subset of the interior of a unit fundamental cube. Their componentwise periodizations \((U,P,F)\) solve Navier–Stokes on the unit flat torus with the same viscosity.

## Nonlinear check

Derivatives commute with the locally finite translation sums. Distinct translated supports, including the supports of derivatives, are separated. Hence
\[
(U\cdot\nabla)U(x,t)
=\sum_{k\in\mathbb Z^n}(u(x+k,t)\cdot\nabla)u(x+k,t),
\]
because cross terms vanish. Every linear term periodizes directly, giving the equation and \(\nabla\cdot U=0\). Pressure is periodized as well, so it is an actual periodic scalar pressure.

## What transfers

Within the original support's fundamental cube, the periodic field equals that single copy. Smoothness, zero initial data, and any local growth sequence there are therefore retained. If the force also has compact time support, so does its periodization. Overlapping supports do not in general preserve the nonlinear equation under the same sum.
