+++
id = "fluid-dynamics/navier-stokes-difference-equation"
title = "Difference equation for two incompressible flows"
kind = "theorem"
summary = "The common force cancels and the nonlinear difference splits into transport and reference-gradient terms."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "fluid-dynamics/quadratic-advection", "real-analysis/divergence-of-tensor", "linear-algebra/outer-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \((u,p)\) and \((v,P)\) solve the [[fluid-dynamics/navier-stokes-equations|incompressible Navier–Stokes equations]] with the same force and viscosity. Set \(w=v-u\) and \(\pi=P-p\). Their **difference equation** is
\[
\partial_t w+(v\cdot\nabla)w+(w\cdot\nabla)u
=\nu\Delta w-\nabla\pi,\qquad \nabla\cdot w=0.
\]
Equivalently, \(\partial_t w+\operatorname{div}g=\nu\Delta w-\nabla\pi\), with \(g=v\otimes v-u\otimes u\) and row divergence \((\operatorname{div}g)_i=\sum_j\partial_jg_{ij}\).

## Exact expansion

The tensor difference is \(g=w\otimes w+w\otimes u+u\otimes w\). Since both velocities are divergence-free, its divergence equals the difference of their advective terms. Expanding \(v=u+w\) proves the nonconservative formula as well. The shared force disappears under subtraction; if forces differ, their difference remains on the right.
