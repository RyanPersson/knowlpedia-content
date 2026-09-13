+++
id = "real-analysis/logarithmic-radial-derivative"
title = "Logarithmic radial derivative"
kind = "definition"
summary = "The dilation derivative r partial_r, equal to differentiation with respect to log r."
aliases = ["dilation derivative", "Euler radial operator"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/natural-logarithm", "real-analysis/exponential-function", "real-analysis/chain-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(r>0\), the **logarithmic radial derivative** is \(D=r\partial_r\). Setting \(s=\log r\) gives
\[
\frac{d}{ds}f(e^s)=(Df)(e^s).
\]
The [[real-analysis/chain-rule|chain rule]] proves this identity. It measures variation under multiplicative changes of radius, and \(D(r^a)=a r^a\).

## Powers of the operator

The product rule gives \(D^2f=r^2f''+rf'\). Consequently
\[
\partial_r^2+r^{-1}\partial_r=r^{-2}D^2,
\qquad
\partial_r^2+r^{-1}\partial_r-r^{-2}=r^{-2}(D^2-1).
\]
Multiplication by powers does not commute with \(D\):
\(D(r^af)=r^a(D+a)f\). These identities are useful for radial equations, but hold on \(r>0\); extension to the axis is a separate regularity question.
