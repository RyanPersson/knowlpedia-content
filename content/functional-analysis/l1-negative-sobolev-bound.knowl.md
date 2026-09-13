+++
id = "functional-analysis/l1-negative-sobolev-bound"
title = "Integrable functions in negative Sobolev spaces"
kind = "theorem"
summary = "An integrable function belongs to H minus s whenever s exceeds half the dimension."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/fourier-sobolev-space", "functional-analysis/regular-tempered-distribution", "measure-theory/lebesgue-integrable-function", "real-analysis/change-of-variables-formula", "functional-analysis/fourier-transform-schwartz-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

If \(f\in L^1(\mathbb R^n)\) and \(s>n/2\), then
\[
\|f\|_{H^{-s}}\le C_{n,s}\|f\|_1.
\]
Thus an integrable function defines an element of the [[functional-analysis/fourier-sobolev-space|negative Sobolev space]] \(H^{-s}\).

## Proof and bounded multipliers

The Fourier integral obeys \(|\widehat f(\xi)|\le\|f\|_1\). The weight integral \(\int(1+4\pi^2|\xi|^2)^{-s}\,d\xi\) is finite precisely for \(2s>n\). Substitution proves the bound. More generally, if \(m\) is bounded and measurable, the inverse Fourier transform of the ordinary function \(m\widehat f\) belongs to \(H^{-s}\) with bound \(C_{n,s}\|m\|_\infty\|f\|_1\). This construction does not require defining multiplication of an arbitrary distribution by a nonsmooth multiplier.
