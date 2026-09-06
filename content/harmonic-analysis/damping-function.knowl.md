+++
id = "harmonic-analysis/damping-function"
title = "Damping function for a frequency set"
kind = "definition"
summary = "A band-limited L2 function with nontrivial local mass, global polynomial decay, and enhanced decay on a prescribed set."
aliases = ["damping function", "Han–Schlag damping function"]
domains = ["harmonic-analysis"]
prerequisites = ["harmonic-analysis/bounded-fourier-support", "analysis/quantitative-unique-continuation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(Y\subseteq\mathbb R^d\) and \(c_1,c_2,c_3,\alpha\in(0,1)\). The set \(Y\)
**admits a damping function with these parameters** if there is
\(\psi\in L^2(\mathbb R^d)\) such that
\[
\operatorname{supp}\widehat\psi\subseteq B_{c_1},\qquad
\|\psi\|_{L^2(B_1)}\ge c_2,
\]
\[
|\psi(x)|\le\langle x\rangle^{-d}\quad(x\in\mathbb R^d),
\qquad
|\psi(x)|\le
\exp\!\left(-c_3\frac{|x|}{(\log(2+|x|))^\alpha}\right)
\quad(x\in Y).
\]
Here \(\langle x\rangle=(1+|x|^2)^{1/2}\).

## Meaning of the four conditions

[[harmonic-analysis/bounded-fourier-support|Bounded Fourier support]] limits
the spectral cost of convolving with \(\psi\). The local \(L^2\) lower bound
prevents the zero function. Polynomial decay makes the function globally
usable, while the final estimate gives substantially faster damping on \(Y\).

## Why \(\alpha<1\)

For \(\alpha>1\), the enhanced bound can hold everywhere for a nonzero
band-limited function and would not record special geometry of \(Y\). The
sublinear logarithmic exponent is the quasi-analytic threshold needed in the
associated [[analysis/quantitative-unique-continuation|quantitative
unique-continuation]] argument.

## References

1. Rui Han and Wilhelm Schlag, “A higher-dimensional Bourgain–Dyatlov fractal uncertainty principle,” *Analysis & PDE* 13 (2020), 813–863. [DOI record](https://doi.org/10.2140/apde.2020.13.813).
2. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Definition 1.5.
