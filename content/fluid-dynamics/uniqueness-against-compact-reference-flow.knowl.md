+++
id = "fluid-dynamics/uniqueness-against-compact-reference-flow"
title = "Uniqueness against a smooth compactly supported reference flow"
kind = "theorem"
summary = "A smooth bounded-energy competitor agrees with a smooth compact reference solution with the same data and force."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/localized-difference-energy-identity", "fluid-dynamics/pressure-gradient-identification", "fluid-dynamics/cutoff-pressure-flux-estimate", "functional-analysis/weighted-cutoff-sobolev-estimate", "convex-analysis/subquadratic-absorption", "differential-equations/gronwall-inequality", "fluid-dynamics/bounded-kinetic-energy", "real-analysis/compactly-supported-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \((u,p)\) be a smooth Navier–Stokes solution on \(\mathbb R^3\times[0,T]\), \(\nu>0\), with the velocity supported in one fixed compact spatial set. If \((v,P)\) is another smooth solution with the same viscosity, force and initial velocity, and \(v\in L^\infty_tL^2_x\), then \(v=u\). The pressure \(P\) may have unrestricted spatial growth.

This is a comparison theorem using [[fluid-dynamics/localized-difference-energy-identity|localized difference energy]], not an existence assertion.

## Pressure first

Set \(w=v-u\) and \(g=v\otimes v-u\otimes u\). Uniform \(L^2\) bounds give \(g\in L^\infty_tL^1_x\). Pressure-gradient identification replaces \(\nabla(P-p)\) by the canonical pressure gradient. Pairing this distributional identity with compactly supported time-space tests replaces the pressure flux in the energy identity by its canonical counterpart for almost every time.

## Absorb the boundary fluxes

Choose \(\phi=1\) near the unit ball, \(0\le\phi\le1\), and set
\[
E_R=\int\phi_R^8|w|^2,\quad A_R=\|\phi_R^4\nabla w\|_2,\quad B_R=\|\phi_R^4w\|_6.
\]
The cutoff Sobolev bound gives \(B_R\le C(A_R+R^{-1}\|w\|_2)\). For large \(R\), the reference velocity vanishes on the cutoff's derivative support, so the transport flux is at most \(C R^{-1}B_R^{3/2}\); the Laplacian flux is at most \(C R^{-2}\). The pressure estimate contributes only powers \(3/2,1/2,3/4\) of \(B_R\). Absorb each subquadratic power into \(\nu A_R^2/2\). Constants may depend on \(T,\nu,u\) and the competitor's energy bound, but not on \(R\). The result is
\[
\frac12 E_R'+\frac\nu2 A_R^2\le\|\nabla u\|_\infty E_R+C/R.
\]
Since \(E_R(0)=0\), Gronwall gives \(E_R(t)\le C_T/R\). On every fixed ball the cutoff equals one for sufficiently large \(R\); taking \(R\to\infty\) proves \(w=0\). Smoothness extends the equality to every time. No global gradient bound for the competitor was assumed.
