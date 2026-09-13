+++
id = "fluid-dynamics/shearing-wave"
title = "Shearing wave on an affine flow"
kind = "construction"
summary = "An exact transverse plane-wave perturbation with a wavevector transported by an affine background."
aliases = ["Kelvin shearing mode", "Craik–Criminale plane wave"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/affine-flow", "fluid-dynamics/navier-stokes-equations", "harmonic-analysis/transverse-polarization", "fluid-dynamics/phase-transport-defect", "fluid-dynamics/viscous-damping-of-a-mode", "linear-algebra/matrix-transpose"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose \(U(t,x)=A(t)x\), with \(\operatorname{tr}A=0\), is a smooth unforced [[fluid-dynamics/navier-stokes-equations|Navier–Stokes]] solution with pressure \(p_U\). Let \(k(t)\in\mathbb R^d\setminus\{0\}\) and \(a(t)\in\mathbb C^d\) solve
\[
k'=-A^T k,\qquad
a'=-Aa+2\frac{k(k\cdot Aa)}{|k|^2}-\nu|k|^2a,
\]
with \(k(0)\cdot a(0)=0\). Then the **shearing wave**
\[
u=U+\operatorname{Re}(a(t)e^{ik(t)\cdot x})
\]
is an exact solution with pressure
\[
p=p_U+\operatorname{Re}\left(\frac{2i(k\cdot Aa)}{|k|^2}e^{ik\cdot x}\right).
\]

## Why the nonlinear wave term vanishes

The wavevector equation transports the phase by \(U\). Differentiating \(k\cdot a\) with the displayed ODEs gives zero, preserving transversality. Since the amplitude is spatially constant and perpendicular to \(k\), every term in \((w\cdot\nabla)w\), for \(w=\operatorname{Re}(ae^{ik\cdot x})\), vanishes. The remaining linear and viscous terms give exactly the amplitude and pressure formulas.

## A simple shear and scope

For \(U=Sx_1e_2\), one has \(k_1(t)=k_1(0)-Stk_2(0)\), with the other components constant. General affine backgrounds use the same displayed evolution. These waves on all of Euclidean space are generally not finite-energy fields. Spatial localization creates additional terms that need correction; the exact plane-wave identity alone does not supply a localized solution.

## References

- [Nishant K. Singh and S. Sridhar, Plane shearing waves of arbitrary form: exact solutions of the Navier–Stokes equations](https://arxiv.org/abs/1101.5507).
