+++
id = "real-analysis/linearization"
title = "Linearization of a nonlinear map"
kind = "definition"
summary = "The derivative at a reference point and the resulting first-order approximation."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/frechet-derivative", "asymptotics/little-o"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a Fréchet differentiable map \(F:U\subset E\to Y\) between real normed spaces, its **linearization at \(u\)** is the operator \(DF(u)\). The associated affine approximation is
\[
F(u+h)=F(u)+DF(u)h+R(u,h),\qquad
\|R(u,h)\|_Y=o(\|h\|_E).
\]
The [[real-analysis/frechet-derivative|Fréchet derivative]] controls all small increments in the stated source norm.

## Linearized equations

To correct a residual \(F(u)\), one may first solve \(DF(u)h=-F(u)\). This cancels the displayed constant and linear terms, leaving \(R(u,h)\). Invertibility and bounds for the inverse need separate proofs. Computing \(\left.\partial_\varepsilon F(u+\varepsilon h)\right|_{\varepsilon=0}\) in each direction gives a candidate linearization; directional derivatives alone do not establish Fréchet differentiability.
