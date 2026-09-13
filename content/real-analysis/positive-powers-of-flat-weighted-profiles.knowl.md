+++
id = "real-analysis/positive-powers-of-flat-weighted-profiles"
title = "Positive powers of flat weighted profiles"
kind = "theorem"
summary = "Two-sided flat-weight control and weighted derivative bounds give smooth zero extension of every fixed positive power."
aliases = ["smooth square root under flat-weight control"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/flat-logarithmic-interval-weight", "real-analysis/real-power", "real-analysis/smooth-zero-extension", "real-analysis/chain-rule-multivariable", "real-analysis/multi-index-notation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(w>0\) be a [[real-analysis/flat-logarithmic-interval-weight|flat interval weight]] in an open interval and let \(\delta\) denote its positive boundary margin. Suppose a smooth positive \(y\), possibly with additional compact parameters, satisfies
\[
y\ge c w,\qquad |\partial^\alpha y|\le C_\alpha w\delta^{-N_\alpha}
\]
for every fixed multi-index, including zero. For every fixed \(r>0\), the function \(y^r\) extends smoothly by zero across the interval endpoints.

## Derivative estimate

Repeated chain and product rules express each derivative as a finite sum of terms
\[
c\,y^{r-j}\prod_{\nu=1}^j\partial^{\alpha_\nu}y,
\qquad |\alpha_\nu|\ge1.
\]
The upper bound on \(y\) controls positive powers; the lower bound controls negative powers. Each term is bounded by \(Cw^r\delta^{-N}\) for some finite \(N\). A positive power of the flat weight beats every such inverse margin power, so all mixed derivatives tend to zero at the boundary. The zero-extension criterion applies. In particular \(r=1/2\) justifies square roots under these quantitative hypotheses.
