+++
id = "fluid-dynamics/navier-stokes-scaling"
title = "Scaling symmetry of Navier–Stokes"
kind = "theorem"
summary = "The parabolic dilation preserving the incompressible Navier–Stokes equations at fixed viscosity."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "real-analysis/chain-rule-multivariable", "real-analysis/anisotropic-dilation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \((u,p,f)\) satisfies the [[fluid-dynamics/navier-stokes-equations|incompressible Navier–Stokes equations]] with kinematic viscosity \(\nu\), then for \(\lambda>0\),
\[
u_\lambda(t,x)=\lambda u(\lambda^2t,\lambda x),\quad
p_\lambda(t,x)=\lambda^2p(\lambda^2t,\lambda x),\quad
f_\lambda(t,x)=\lambda^3f(\lambda^2t,\lambda x)
\]
satisfies the same equations with the same \(\nu\) on the correspondingly rescaled domain.

## Verification

Each of \(\partial_tu_\lambda\), \((u_\lambda\cdot\nabla)u_\lambda\), \(\nabla p_\lambda\), and \(\nu\Delta u_\lambda\) equals \(\lambda^3\) times the original term at \((\lambda^2t,\lambda x)\). The divergence equals \(\lambda^2(\nabla\cdot u)\) there and remains zero. Initial data transform as \(u_{\lambda,0}(x)=\lambda u_0(\lambda x)\).

## Integral scaling

In dimension \(d\), kinetic energy scales as \(E_\lambda(t)=\lambda^{2-d}E(\lambda^2t)\). More generally, on \(I_\lambda=\lambda^{-2}I\),
\[
\|u_\lambda\|_{L^p_t(I_\lambda;L^q_x)}
=\lambda^{1-2/p-d/q}\|u\|_{L^p_t(I;L^q_x)}.
\]
The exponent is zero when \(2/p+d/q=1\); such a norm is called scaling critical. These identities require the indicated norms to be defined.

## References

- [Charles Fefferman, Existence and Smoothness of the Navier–Stokes Equation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
