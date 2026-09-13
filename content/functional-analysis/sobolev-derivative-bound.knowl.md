+++
id = "functional-analysis/sobolev-derivative-bound"
title = "Derivative bound between Fourier Sobolev spaces"
kind = "theorem"
summary = "Each distributional derivative lowers the Sobolev order by its degree."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/fourier-sobolev-space", "functional-analysis/distributional-derivative", "real-analysis/multi-index-notation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For real \(s\) and a multi-index \(\alpha\), distributional differentiation is a bounded map
\[
\partial^\alpha:H^s(\mathbb R^n)\longrightarrow H^{s-|\alpha|}(\mathbb R^n),\qquad
\|\partial^\alpha u\|_{H^{s-|\alpha|}}\le\|u\|_{H^s}.
\]
Here \(H^s\) uses the [[functional-analysis/fourier-sobolev-space|Fourier weight]] \((1+4\pi^2|\xi|^2)^s\).

## Fourier proof

The derivative multiplies \(\widehat u\) by \((2\pi i\xi)^\alpha\), whose absolute value is at most \((1+4\pi^2|\xi|^2)^{|\alpha|/2}\). Insert this inequality in the norm. The same definition shows \(H^{s_1}\subset H^{s_2}\) continuously when \(s_1\ge s_2\).
