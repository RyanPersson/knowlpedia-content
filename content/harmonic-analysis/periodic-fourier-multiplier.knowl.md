+++
id = "harmonic-analysis/periodic-fourier-multiplier"
title = "Periodic Fourier multiplier"
kind = "definition"
summary = "An operator defined by multiplying each periodic Fourier coefficient by a prescribed symbol."
aliases = ["Fourier multiplier on a torus"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-coefficient", "harmonic-analysis/fourier-series", "linear-algebra/linear-map", "harmonic-analysis/fourier-character"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A **periodic Fourier multiplier** with symbol \(a:\mathbb Z^d\to\mathbb C\) acts on a finite Fourier sum by
\[
T_a\left(\sum_m c_m e_m\right)=\sum_m a(m)c_m e_m.
\]
It is a linear operator diagonal in the [[harmonic-analysis/fourier-character|Fourier characters]]. Extending it to a function space requires a convergence and boundedness statement.

## Standard symbols

The derivative \(\partial_{x_j}\) has symbol \(2\pi i m_j\); the Laplacian has symbol \(-4\pi^2|m|^2\). Subtracting the mean has symbol zero at \(m=0\) and one elsewhere. For a constant direction \(v\), formally inverting \(v\cdot\nabla\) uses \((2\pi i v\cdot m)^{-1}\) at nonzero denominators. Resonances and small denominators require additional analysis.
