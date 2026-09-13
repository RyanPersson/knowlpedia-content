+++
id = "harmonic-analysis/fourier-character"
title = "Fourier character on the standard torus"
kind = "definition"
summary = "An integer-frequency periodic complex exponential."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/periodic-function", "real-analysis/exponential-function", "linear-algebra/inner-product", "shared-foundations/integers", "shared-foundations/quotient-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(m\in\mathbb Z^d\), the **Fourier character** is the [[real-analysis/periodic-function|periodic function]]
\[
e_m(x)=\exp(2\pi i\,m\cdot x),\qquad x\in\mathbb R^d.
\]
It is unchanged by every integer translation, so it defines a function on \(\mathbb R^d/\mathbb Z^d\). It obeys \(e_m(x+y)=e_m(x)e_m(y)\) and \(|e_m|=1\).

## Algebra and normalization

The exponential identity gives \(e_me_n=e_{m+n}\) and \(\overline{e_m}=e_{-m}\). In an angular coordinate \(\theta\) of period \(2\pi\), the corresponding characters are \(e^{im\theta}\). They are concrete examples of [[harmonic-analysis/unitary-character|unitary characters]]; specifying the coordinate period fixes where the factor \(2\pi\) occurs.

## References

- [Leonid Ryzhik, Lecture notes for Math 205A, Chapters 8–9](https://math.stanford.edu/~ryzhik/STANFORD/STANF205-11/notes-205.pdf).
