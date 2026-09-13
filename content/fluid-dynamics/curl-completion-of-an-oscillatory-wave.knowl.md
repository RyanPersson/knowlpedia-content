+++
id = "fluid-dynamics/curl-completion-of-an-oscillatory-wave"
title = "Curl completion of a transverse oscillatory wave"
kind = "construction"
summary = "A vector potential producing an exactly divergence-free wave with a lower-order curl correction."
aliases = ["curl remainder", "solenoidal wave correction"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/transverse-polarization", "real-analysis/curl", "real-analysis/vector-potential", "linear-algebra/cross-product", "real-analysis/quotient-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(a:U\to\mathbb C^3\) and \(\Phi:U\to\mathbb R\) be smooth, with \(n=\nabla\Phi\ne0\), \(n\cdot a=0\), and real \(\kappa\ne0\). Define
\[
W=\nabla\times\left(\frac{i}{\kappa}\frac{n\times a}{|n|^2}e^{i\kappa\Phi}\right).
\]
Then \(\nabla\cdot W=0\), and
\[
W=e^{i\kappa\Phi}\left(a+
\frac{i}{\kappa}\nabla\times\frac{n\times a}{|n|^2}\right).
\]
Cross products with complex amplitudes use the complex bilinear extension of the real cross product. This is a **curl completion** of the [[harmonic-analysis/transverse-polarization|transverse]] principal amplitude \(a\).

## Verification and size of the correction

Use \(\nabla\times(b e^{i\kappa\Phi})=e^{i\kappa\Phi}(\nabla\times b+i\kappa n\times b)\) and \(n\times(n\times a)=-|n|^2a\). Divergence of a curl vanishes. With a positive lower bound for \(|n|\) and bounds on derivatives of \(n,a\), the displayed correction coefficient has an explicit factor \(\kappa^{-1}\). Derivatives of the full corrected wave also differentiate the exponential and need separate estimates. Smoothly supported vector potentials preserve support under this construction.
