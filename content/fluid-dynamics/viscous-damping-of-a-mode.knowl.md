+++
id = "fluid-dynamics/viscous-damping-of-a-mode"
title = "Viscous damping of a Fourier mode"
kind = "definition"
summary = "The exponential decay produced by viscosity at a specified spatial wavevector."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/viscosity", "harmonic-analysis/wavevector", "differential-equations/integrating-factor", "real-analysis/laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a fixed [[harmonic-analysis/wavevector|wavevector]] \(k\), the mode \(w(t,x)=a(t)e^{ik\cdot x}\) satisfies \(\partial_tw=\nu\Delta w\) exactly when
\[
a'=-\nu|k|^2a,
\qquad a(t)=e^{-\nu|k|^2(t-s)}a(s).
\]
This is **viscous damping** at rate \(\nu|k|^2\), since \(\Delta e^{ik\cdot x}=-|k|^2e^{ik\cdot x}\).

## A varying wavevector

If an amplitude equation has scalar damping \(-\nu|k(t)|^2a\), its damping factor is \(\exp(-\nu\int_s^t|k(r)|^2\,dr)\). Other matrix terms can simultaneously amplify or rotate the amplitude. For \(e^{i\kappa m\Phi}\), the leading viscous rate is \(\nu\kappa^2m^2|\nabla\Phi|^2\); lower-order amplitude and phase derivatives remain in the full Laplacian.

## References

- [Nishant K. Singh and S. Sridhar, Plane shearing waves of arbitrary form: exact solutions of the Navier–Stokes equations](https://arxiv.org/abs/1101.5507).
