+++
id = "harmonic-analysis/zero-fourier-mode"
title = "Zero Fourier mode"
kind = "definition"
summary = "The constant component of a periodic Fourier expansion, equal to its normalized mean."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-coefficient", "harmonic-analysis/fourier-character"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **zero Fourier mode** of an integrable periodic function is the constant function \(\widehat f(0)e_0=\widehat f(0)\). On a unit cell,
\[
\widehat f(0)=\int_{[0,1]^d}f(x)\,dx.
\]
Thus the zero [[harmonic-analysis/fourier-coefficient|coefficient]] is the normalized mean.

## Partial averaging

For \(f(x,y)\), taking the zero mode only in \(y\) leaves a function of \(x\). Saying that a coefficient has zero frequency in one angular variable does not imply independence of every auxiliary variable.
