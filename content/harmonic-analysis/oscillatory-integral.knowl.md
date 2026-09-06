+++
id = "harmonic-analysis/oscillatory-integral"
title = "Oscillatory integral"
kind = "definition"
summary = "An integral with a rapidly varying phase whose cancellation, rather than absolute size, governs its asymptotics."
aliases = ["oscillatory integral operator"]
domains = ["harmonic-analysis", "partial-differential-equations", "microlocal-analysis"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **oscillatory integral** with large parameter \(\lambda\) has the form
\[
I(\lambda)=\int_{\mathbb R^n}e^{i\lambda\phi(x)}a(x)\,dx,
\]
where the real-valued function \(\phi\) is the phase and \(a\) is the
amplitude. The term may also denote an operator obtained by allowing the phase
and amplitude to depend on input and output variables.

## Cancellation

Away from [[real-analysis/critical-point|critical points]] of \(\phi\), [[real-analysis/integration-by-parts|integration by parts]] gives decay faster
than the absolute-value estimate. Near nondegenerate critical points,
stationary phase gives an asymptotic expansion whose leading order is
\(\lambda^{-n/2}\).

## Fourier-like relations

Fourier transformation is the model oscillatory integral. In quantum chaos,
incoming and outgoing boundary data are related by oscillatory integral
operators, so simultaneous localization becomes a
[[harmonic-analysis/fractal-uncertainty-principle|fractal uncertainty]]
question.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2).
