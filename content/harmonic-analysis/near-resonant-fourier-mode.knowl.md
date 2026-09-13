+++
id = "harmonic-analysis/near-resonant-fourier-mode"
title = "Nearly resonant Fourier mode"
kind = "definition"
summary = "A nonresonant directional Fourier mode whose eigenvalue is small relative to a chosen tolerance."
aliases = ["near resonance", "nearly resonant mode"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/resonant-fourier-mode", "real-analysis/absolute-value"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Fix a direction \(v\), a frequency range \(\mathcal M\subset\mathbb Z^n\setminus\{0\}\), and a tolerance \(\delta>0\). A mode \(m\in\mathcal M\) is **nearly resonant** at tolerance \(\delta\) for \(v\cdot\nabla\) if
\[
0<|v\cdot m|\le\delta.
\]
The positive lower inequality excludes an [[harmonic-analysis/resonant-fourier-mode|exact resonance]]. Other normalizations may compare \(|v\cdot m|\) to a frequency-dependent threshold; the convention must be specified.

## Effect on inversion

Solving the mode equation divides the forcing coefficient by \(2\pi i(v\cdot m)\), which may amplify it strongly. “Nearly resonant” without a scale or tolerance is only a qualitative description. A Diophantine lower bound controls how small these nonzero divisors can be as frequency increases.
