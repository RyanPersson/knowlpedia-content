+++
id = "real-analysis/cutoff-of-a-controlled-scale"
title = "Derivatives of a cutoff composed with a controlled scale"
kind = "theorem"
summary = "Scale derivatives compensate for large cutoff parameters on the transition region."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cutoff-function", "real-analysis/chain-rule-multivariable", "real-analysis/multi-index-notation", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(q:\Omega\to(0,1]\) be smooth and suppose for a fixed \(c>0\) that
\[
|\partial^\alpha q|\le C_\alpha q^{1-c|\alpha|}\qquad(|\alpha|\ge1).
\]
If \(\chi\) is smooth, equals one on \([0,1/2]\), and vanishes on \([1,\infty)\), then for \(a>0\),
\[
|\partial^\alpha[\chi(aq)]|\le C_{\alpha,\chi}q^{-c|\alpha|},
\]
with constants independent of \(a\). This is the [[real-analysis/chain-rule-multivariable|chain rule]] on the cutoff transition.

## Cancellation of the cutoff parameter

For positive derivative order, every term has the form \(a^k\chi^{(k)}(aq)\prod_{r=1}^k\partial^{\beta_r}q\), with \(\sum_r|\beta_r|=|\alpha|\). Its support has \(1/2\le aq\le1\). The derivatives of \(q\) contribute \(q^{k-c|\alpha|}\), and \(a^kq^k\) is bounded there. Order zero uses only boundedness of \(\chi\). An anisotropic assumption \(|\partial^\alpha q|\le C_\alpha q^{1-\sum_i c_i\alpha_i}\) gives the corresponding anisotropic loss by the same proof.
