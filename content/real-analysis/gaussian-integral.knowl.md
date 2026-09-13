+++
id = "real-analysis/gaussian-integral"
title = "Gaussian integral"
kind = "theorem"
summary = "The integral of exp minus a positive multiple of the square is the square root of pi divided by that multiple."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function", "real-analysis/nonnegative-square-root", "measure-theory/tonellis-theorem", "real-analysis/change-of-variables-formula", "real-analysis/cylindrical-coordinates", "real-analysis/pi", "measure-theory/monotone-convergence-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(a>0\), the **Gaussian integral** is
\[
\int_{\mathbb R}e^{-ax^2}\,dx=\sqrt{\pi/a}.
\]
Its product form is \(\int_{\mathbb R^n}e^{-a|x|^2}\,dx=(\pi/a)^{n/2}\), by [[measure-theory/tonellis-theorem|Tonelli's theorem]].

## Planar proof

The integral for \(a=1\) is finite and positive. Its square equals \(\int_{\mathbb R^2}e^{-(x^2+y^2)}\,dx\,dy\). In polar coordinates this becomes \(2\pi\int_0^\infty e^{-r^2}r\,dr=\pi\). Taking the positive square root gives \(\sqrt\pi\); substitution \(y=\sqrt a\,x\) gives the general case.
