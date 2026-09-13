+++
id = "harmonic-analysis/resonant-fourier-mode"
title = "Resonant mode of a directional derivative"
kind = "definition"
summary = "A Fourier mode on which a specified constant directional derivative vanishes."
aliases = ["directional Fourier resonance"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-character", "real-analysis/directional-derivative", "linear-algebra/inner-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(D_v=v\cdot\nabla\) on the unit torus, a [[harmonic-analysis/fourier-character|Fourier mode]] \(m\in\mathbb Z^n\) is **resonant** if \(v\cdot m=0\), since
\[
D_v e^{2\pi i m\cdot x}=2\pi i(v\cdot m)e^{2\pi i m\cdot x}.
\]
The zero mode is always resonant. A nonzero resonant mode is an additional obstruction to solving \(D_vu=f\): the corresponding Fourier coefficient of \(f\) must vanish.

## Near resonance

A [[harmonic-analysis/near-resonant-fourier-mode|nearly resonant mode]] has a small nonzero eigenvalue relative to a specified tolerance. It need not lie in the kernel.
