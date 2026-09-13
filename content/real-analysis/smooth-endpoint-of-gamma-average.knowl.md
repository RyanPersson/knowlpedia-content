+++
id = "real-analysis/smooth-endpoint-of-gamma-average"
title = "Smooth nonanalytic endpoint of a Gamma average"
kind = "theorem"
summary = "All one-sided derivatives of the Gamma average exist at zero, although its Taylor series has zero radius of convergence."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/gamma-average-profile", "shared-foundations/rising-factorial", "measure-theory/differentiation-under-integral", "real-analysis/taylors-theorem-with-remainder", "real-analysis/real-analytic-function", "real-analysis/ratio-test"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(a,b>0\), the [[real-analysis/gamma-average-profile|Gamma average]] \(F=F_{a,b}\) is smooth up to \(z=0\) from the right, with
\[
F^{(m)}(0)=(-1)^m(a)_m(b)_m.
\]
Here \((a)_m\) is the rising factorial. Its Taylor series at zero has radius of convergence zero, so this endpoint smoothness is not real analyticity.

## Differentiation and finite remainders

Differentiation under the integral gives
\[
F^{(m)}(z)=\frac{(-1)^m(b)_m}{\Gamma(a)}
\int_0^\infty e^{-v}v^{a+m-1}(1+zv)^{-b-m}\,dv.
\]
Deleting the last factor gives an integrable bound valid for \(z\ge0\). Thus \(|F^{(m)}(z)|\le(a)_m(b)_m\), and finite Taylor expansions have the usual remainder bounds. For example, \(|F(z)-1+abz|\le(a)_2(b)_2z^2/2\).

The absolute Taylor coefficients are \((a)_m(b)_m/m!\); the ratio of consecutive coefficients is \((a+m)(b+m)/(m+1)\), which tends to infinity. This proves the zero convergence radius. Fixed-order differentiated remainder estimates remain valid and do not require summing that divergent series.
