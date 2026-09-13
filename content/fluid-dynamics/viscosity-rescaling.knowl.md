+++
id = "fluid-dynamics/viscosity-rescaling"
title = "Rescaling unit viscosity to positive viscosity"
kind = "lemma"
summary = "A spatial and amplitude change that converts a unit-viscosity solution to viscosity nu."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "real-analysis/chain-rule-multivariable", "real-analysis/nonnegative-square-root"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \((u_1,p_1,f_1)\) solve the [[fluid-dynamics/navier-stokes-equations|Navier–Stokes equations]] with viscosity \(1\). For \(\nu>0\), set
\[
u_\nu(t,x)=\sqrt\nu\,u_1(t,x/\sqrt\nu),\quad
p_\nu(t,x)=\nu p_1(t,x/\sqrt\nu),\quad
f_\nu(t,x)=\sqrt\nu\,f_1(t,x/\sqrt\nu).
\]
Then \((u_\nu,p_\nu,f_\nu)\) solves the equations with viscosity \(\nu\).

## Verification and energy

The time, advection, pressure, and viscous terms all become \(\sqrt\nu\) times their unit-viscosity versions. Divergence remains zero. By change of variables, the kinetic energy in dimension \(d\) is \(E_\nu(t)=\nu^{1+d/2}E_1(t)\), whenever finite. The spatial domain is also dilated by \(\sqrt\nu\); on a torus this changes its periods.

## References

- [Charles Fefferman, Existence and Smoothness of the Navier–Stokes Equation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
