+++
id = "harmonic-analysis/riesz-transform"
title = "Riesz transform"
kind = "definition"
summary = "The order-zero Euclidean multiplier i times a frequency coordinate divided by frequency length."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/euclidean-l2-fourier-multiplier", "linear-algebra/euclidean-norm", "shared-foundations/complex-numbers-c"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

On \(L^2(\mathbb R^n)\), the **Riesz transform** \(R_j\), \(1\le j\le n\), is the [[harmonic-analysis/euclidean-l2-fourier-multiplier|Fourier multiplier]]
\[
\widehat{R_jf}(\xi)=\frac{i\xi_j}{|\xi|}\widehat f(\xi),\qquad \xi\ne0.
\]
The symbol may be assigned any value at zero, a null set. This entry uses the plus-\(i\) convention; the alternative minus-\(i\) convention reverses each individual transform.

## Products and integrability

The double transform has symbol \(-\xi_i\xi_j/|\xi|^2\), unchanged if the sign convention for all single transforms is reversed. Riesz transforms extend boundedly to \(L^p\) for \(1<p<\infty\), by singular-integral theory. This does not give a bounded map \(L^1\to L^1\). A bounded frequency formula for a specific \(L^1\) input can instead be interpreted as a negative-order Sobolev distribution.

## References

- [Tao, Fourier analysis lecture notes 4, §§2 and 4](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf).
