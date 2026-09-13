+++
id = "harmonic-analysis/fourier-product-mean"
title = "Mean of a product of periodic Fourier sums"
kind = "lemma"
summary = "Only pairs of opposite frequencies contribute to the average of a product without conjugation."
aliases = ["angular harmonic cancellation"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-orthogonality", "harmonic-analysis/fourier-coefficient", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For finite Fourier sums \(f=\sum_m a_m e_m\) and \(g=\sum_n b_n e_n\),
\[
\int_{[0,1]^d}f(x)g(x)\,dx=\sum_m a_m b_{-m}.
\]
This follows by expanding the product and applying [[harmonic-analysis/fourier-orthogonality|orthogonality without conjugation]]. The same identity holds for smooth periodic functions by absolute convergence.

## A real oscillatory pair

For a nonzero frequency and complex vectors \(a,b\) independent of the averaging variable,
\[
\left\langle (ae_m+\bar a e_{-m})\otimes(be_m+\bar b e_{-m})\right\rangle
=a\otimes\bar b+\bar a\otimes b.
\]
Using \(\operatorname{Re}(ae_m)\) instead introduces a factor \(1/4\) in this displayed product. If amplitudes themselves depend on the averaging variable, their frequencies must also be included; one cannot treat them as constants.
