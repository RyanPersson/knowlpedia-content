+++
id = "fluid-dynamics/localized-difference-energy-identity"
title = "Localized difference-energy identity"
kind = "theorem"
summary = "A compact spatial weight exposes the transport and pressure fluxes in the energy of two flows."
aliases = ["cutoff difference-energy identity"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/navier-stokes-difference-equation", "fluid-dynamics/relative-kinetic-energy", "real-analysis/cutoff-function", "real-analysis/integration-by-parts"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For smooth solutions with common force and viscosity, let \(w=v-u\), \(\pi=P-p\), and let \(\chi\) be a smooth, time-independent compactly supported scalar weight. The [[fluid-dynamics/navier-stokes-difference-equation|difference equation]] gives
\[
\begin{aligned}
\frac12\frac d{dt}\int\chi|w|^2+\nu\int\chi|\nabla w|^2
={}&-\int\chi\,(w\cdot\nabla)u\cdot w
+\frac\nu2\int|w|^2\Delta\chi\\
&+\frac12\int|w|^2v\cdot\nabla\chi
+\int\pi w\cdot\nabla\chi.
\end{aligned}
\]
All integrals are over space. Compact support of \(\chi\) makes them local; no decay at infinity is needed.

## Derivation

Pair the difference equation with \(\chi w\). Integrating the Laplacian by parts twice gives the weighted gradient term and \(\tfrac\nu2\int|w|^2\Delta\chi\). Incompressibility moves the transport and pressure derivatives onto \(\chi\). The reference-gradient term remains because the derivative acts on \(u\), not on the energy density.
