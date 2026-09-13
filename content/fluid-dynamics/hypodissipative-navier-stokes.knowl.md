+++
id = "fluid-dynamics/hypodissipative-navier-stokes"
title = "Hypodissipative Navier–Stokes equations"
kind = "definition"
summary = "Incompressible momentum with a positive fractional dissipation order less than the usual Laplacian."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "harmonic-analysis/fractional-laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **hypodissipative Navier–Stokes equations** with exponent \(0<\alpha<1\) and \(\nu>0\) are
\[
\partial_tu+(u\cdot\nabla)u+\nabla p
=-\nu(-\Delta)^\alpha u+f,\qquad\operatorname{div}u=0.
\]
The [[harmonic-analysis/fractional-laplacian|fractional Laplacian]] replaces the second-order dissipation of [[fluid-dynamics/navier-stokes-equations|Navier–Stokes]]. Its differential order is \(2\alpha<2\).

## Exponent conventions

If the dissipative term is written \(-\nu|\nabla|^\beta u\), then \(\beta=2\alpha\). A parameter range stated for \(\beta\) cannot be read as the same range for \(\alpha\). The endpoint \(\alpha=1\) recovers ordinary viscosity; it is outside the strict hypodissipative range used here.

## References

- [Córdoba, Martínez-Zoroa and Zheng, Finite time blow-up for the hypodissipative Navier Stokes equations with a smooth source](https://arxiv.org/abs/2407.06776).
