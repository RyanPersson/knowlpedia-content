+++
id = "fluid-dynamics/change-of-viscosity-by-spatial-rescaling"
title = "Changing viscosity by spatial rescaling"
kind = "theorem"
summary = "A spatial dilation and matched amplitude change transport a solution between positive viscosities without changing time."
aliases = ["viscosity normalization"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-equations", "real-analysis/chain-rule-multivariable", "real-analysis/change-of-variables-formula", "fluid-dynamics/viscous-dissipation", "real-analysis/nonnegative-square-root"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Suppose \((u,p,f)\) solves the [[fluid-dynamics/navier-stokes-equations|Navier–Stokes equations]] with viscosity \(\nu_0>0\). For a desired \(\nu>0\), set \(a=\sqrt{\nu/\nu_0}\) and
\[
u^{(\nu)}(x,t)=a u(x/a,t),\quad
p^{(\nu)}(x,t)=a^2p(x/a,t),\quad
f^{(\nu)}(x,t)=a f(x/a,t).
\]
These fields solve the equations with viscosity \(\nu\). Time and its endpoints are unchanged.

## Verification and norms

The time derivative, advection, pressure gradient, and force each acquire a factor \(a\). The diffusion term is \(\nu a^{-1}\Delta u=a\nu_0\Delta u\). The divergence is the original divergence at \(x/a\). In dimension \(n\),
\[
\|u^{(\nu)}(t)\|_2^2=a^{n+2}\|u(t)\|_2^2,\qquad
\nu\int\!\|\nabla u^{(\nu)}\|_2^2dt
=a^{n+2}\nu_0\int\!\|\nabla u\|_2^2dt.
\]
A spatial support \(K\) becomes \(aK\), and \(\partial_x^\alpha\partial_t^m f^{(\nu)}=a^{1-|\alpha|}(\partial_x^\alpha\partial_t^m f)(x/a,t)\). These are bounds for each fixed positive viscosity, not assertions uniform as \(\nu\to0\).
