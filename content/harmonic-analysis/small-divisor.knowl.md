+++
id = "harmonic-analysis/small-divisor"
title = "Small divisor"
kind = "definition"
summary = "A small nonzero spectral denominator that amplifies coefficients when a linear equation is inverted."
aliases = ["small-divisor problem"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/periodic-fourier-multiplier", "harmonic-analysis/resonant-fourier-mode"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose a diagonal [[harmonic-analysis/periodic-fourier-multiplier|Fourier multiplier]] equation reads \(\lambda_m\widehat u(m)=\widehat f(m)\). A **small divisor** is a nonzero denominator \(\lambda_m\) whose small size makes
\[
\widehat u(m)=\widehat f(m)/\lambda_m
\]
large relative to the input coefficient. A small-divisor problem concerns controlling these inverses across the frequency set.

## Directional derivatives

For \(v\cdot\nabla\), the denominators are \(2\pi i(v\cdot m)\). Exact zeros are [[harmonic-analysis/resonant-fourier-mode|resonances]] requiring compatibility. Nonzero denominators bounded below by a reciprocal polynomial yield at most polynomial coefficient growth under inversion; faster decay of denominators can cause more severe regularity loss. Nonvanishing alone is not a uniform estimate.
