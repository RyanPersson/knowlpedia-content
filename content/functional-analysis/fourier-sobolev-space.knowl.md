+++
id = "functional-analysis/fourier-sobolev-space"
title = "Fourier Sobolev space on Euclidean space"
kind = "definition"
summary = "A tempered distribution whose Fourier transform is square integrable with a prescribed polynomial weight."
aliases = ["inhomogeneous Sobolev space", "negative-order Sobolev space", "Bessel potential space H^s"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/tempered-distribution", "functional-analysis/fourier-transform-tempered-distributions", "measure-theory/lp-space", "real-analysis/real-power", "linear-algebra/euclidean-norm", "real-analysis/pi"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For real \(s\), the **Fourier Sobolev space** \(H^s(\mathbb R^n)\) consists of [[functional-analysis/tempered-distribution|tempered distributions]] \(u\) whose Fourier transform is represented by a measurable function and satisfies
\[
\|u\|_{H^s}^2=\int_{\mathbb R^n}(1+4\pi^2|\xi|^2)^s|\widehat u(\xi)|^2\,d\xi<\infty.
\]
The Fourier convention is \(\widehat f(\xi)=\int e^{-2\pi ix\cdot\xi}f(x)\,dx\). Negative \(s\) are allowed; their weights decay at high frequency.

## Integer orders and duality

Plancherel's theorem and \(\widehat{\partial_j u}=2\pi i\xi_j\widehat u\) identify \(H^k\), for nonnegative integers \(k\), with \(W^{k,2}(\mathbb R^n)\) with equivalent norms. Replacing \(1+4\pi^2|\xi|^2\) by \(1+|\xi|^2\) also gives an equivalent norm. The pairing extending the \(L^2\) inner product identifies \(H^{-s}\) with the continuous dual of \(H^s\). Cauchy–Schwarz in Fourier space gives \(|\langle u,v\rangle|\le\|u\|_{H^{-s}}\|v\|_{H^s}\).

## Low-frequency condition

These are inhomogeneous spaces: the weight stays positive near \(\xi=0\). A delta distribution in frequency is not a weighted \(L^2\) function. In particular, a nonzero constant function on the whole space belongs to no \(H^s(\mathbb R^n)\), even when \(s<0\).
