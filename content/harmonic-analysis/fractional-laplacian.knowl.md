+++
id = "harmonic-analysis/fractional-laplacian"
title = "Fractional Laplacian on Euclidean space"
kind = "definition"
summary = "The Fourier operator with symbol (2 pi times frequency magnitude) to the power twice alpha."
aliases = ["fractional dissipation", "absolute gradient power"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/fourier-transform-schwartz-space", "functional-analysis/fourier-transform-tempered-distributions", "functional-analysis/schwartz-space", "real-analysis/real-power", "real-analysis/laplacian", "real-analysis/pi"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(\alpha>0\), the **fractional Laplacian** on \(\mathbb R^n\) is defined first for [[functional-analysis/schwartz-space|Schwartz functions]] by
\[
\widehat{(-\Delta)^\alpha f}(\xi)=(2\pi|\xi|)^{2\alpha}\widehat f(\xi),
\]
using the [[functional-analysis/fourier-transform-schwartz-space|Fourier convention]] \(\widehat f(\xi)=\int e^{-2\pi i x\cdot\xi}f(x)\,dx\). The [[real-analysis/real-power|power]] times \(\widehat f\) defines a tempered distribution, so [[functional-analysis/fourier-transform-tempered-distributions|distributional Fourier inversion]] defines the output. At \(\alpha=1\) this is the negative [[real-analysis/laplacian|Laplacian]]. The notation \(|\nabla|^\beta\) means \((-\Delta)^{\beta/2}\).

The constant [[real-analysis/pi|\(\pi\)]] appears because frequencies are measured in cycles per unit length.

## Positive quadratic form

Plancherel gives \(\langle f,(-\Delta)^\alpha f\rangle=\int(2\pi|\xi|)^{2\alpha}|\widehat f|^2\geq0\). For noninteger \(\alpha\) the symbol need not be smooth at zero, so this formula is not a license to multiply every tempered distribution by the symbol. On \(L^2\), the natural operator domain consists of functions for which the displayed product belongs to \(L^2\).
