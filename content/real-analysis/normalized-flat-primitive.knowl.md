+++
id = "real-analysis/normalized-flat-primitive"
title = "Normalized primitive of an exponential flat factor"
kind = "theorem"
summary = "Dividing an integral containing exp(-c/t²) by the same exponential leaves a smooth coefficient times a cubic power."
aliases = ["exponential flat-factor integration lemma"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/flat-exponential", "real-analysis/change-of-variables-formula", "measure-theory/differentiation-under-integral", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Fix \(c>0\), an integer \(j\ge0\), and a smooth function \(b(y,\eta)\) for \(|y|<\varepsilon\), \(\eta\in U\subseteq\mathbb R^d\). For \(0<y<\varepsilon\), define
\[
H(y,\eta)=e^{c/y^2}\int_0^y e^{-c/u^2}u^j b(u,\eta)\,du.
\]
Then \(H(y,\eta)=y^{j+3}B(y,\eta)\), where \(B\) extends smoothly through \(y=0\) and
\[
B(0,\eta)=\frac{b(0,\eta)}{2c}.
\]

## Fixed-domain integral proof

Use the [[real-analysis/change-of-variables-formula|substitution]] \(s=u^{-2}-y^{-2}\). It gives
\[
B(y,\eta)=\frac12\int_0^\infty e^{-cs}
(1+y^2s)^{-(j+3)/2}
b\!\left(\frac{y}{\sqrt{1+y^2s}},\eta\right)\,ds.
\]
The right side is defined for both signs of small \(y\). On compact parameter sets, every derivative of its integrand is bounded by \(C(1+s)^N e^{-cs}\), for some \(C,N\) depending on that derivative. This is integrable, so [[measure-theory/differentiation-under-integral|differentiation under the integral]] proves smoothness. Set \(y=0\) to obtain the stated boundary value.

## Positive smooth multipliers

If \(a(y)=e^{-c/y^2}g(y)\) for \(y>0\), with \(g\) smooth and \(g(0)>0\), then
\[
\frac1{a(y)}\int_0^y a(u)u^j b(u,\eta)\,du
\]
also equals \(y^{j+3}\) times a smooth coefficient near zero. Apply the formula with \(gb\) and divide the resulting coefficient by the nonvanishing function \(g(y)\). This conclusion uses the specific exponential profile, not just flatness.
