+++
id = "fluid-dynamics/delayed-parabolic-rescaling"
title = "Delayed parabolic rescaling at a fixed terminal time"
kind = "theorem"
summary = "Parabolic scaling combined with a time shift shrinks spatial support while retaining a chosen terminal time."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-scaling", "real-analysis/smooth-zero-extension", "shared-foundations/support-of-a-function", "real-analysis/chain-rule-multivariable", "real-analysis/compactly-supported-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let smooth Navier–Stokes fields \((u,p,f)\) be defined for \(0\le s<T\), vanish for \(s\) in an initial neighborhood of zero, and have a fixed compact spatial support. For \(\lambda\ge1\), put \(t_0=T(1-\lambda^{-2})\). On \(t_0\le t<T\), define
\[
\widetilde u(x,t)=\lambda u(\lambda x,\lambda^2(t-t_0)),\quad
\widetilde p(x,t)=\lambda^2p(\lambda x,\lambda^2(t-t_0)),\quad
\widetilde f(x,t)=\lambda^3f(\lambda x,\lambda^2(t-t_0)).
\]
Extending all three by zero for \(t<t_0\) gives smooth fields satisfying the same equation and viscosity. This uses the [[fluid-dynamics/navier-stokes-scaling|parabolic scaling symmetry]].

## Support and endpoint

The initial vanishing makes the time gluing smooth. A spatial support \(K\) shrinks to \(\lambda^{-1}K\), while \(\lambda^2(T-t_0)=T\), so the old terminal time is reached at the same new terminal time. If the original force is defined smoothly for later \(s\), its displayed rescaling is used there as well. This rescaling can place all supports inside a fundamental cube before periodization.
