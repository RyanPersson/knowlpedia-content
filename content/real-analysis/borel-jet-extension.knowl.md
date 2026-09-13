+++
id = "real-analysis/borel-jet-extension"
title = "Borel extension of a prescribed smooth jet"
kind = "theorem"
summary = "Arbitrary smooth coefficients can be realized as all normal derivatives of one smooth function."
aliases = ["Borel's lemma", "smooth jet realization"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cartesian-jet", "real-analysis/cutoff-function", "real-analysis/scaled-cutoff-estimate", "analysis/smooth-series-convergence", "shared-foundations/factorial", "topology/compact-exhaustion"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(U\subseteq\mathbb R^n\) be open and \(a_j\in C^\infty(U)\) for every integer \(j\ge0\). There exists \(F\in C^\infty(U\times\mathbb R)\) such that
\[
\partial_t^jF(x,0)=a_j(x)\qquad(j\ge0).
\]
This is **Borel's smooth jet extension theorem**, with \(x\) as a parameter. No growth bound on the sequence \((a_j)\) is required.

## Shrinking-cutoff construction

Choose \(\chi\in C_c^\infty(\mathbb R)\), supported in \([-1,1]\), equal to one near zero. Set
\[
F(x,t)=\sum_{j=0}^\infty
\chi(t/\varepsilon_j)\,a_j(x)\frac{t^j}{j!}.
\]
Take a compact exhaustion \((K_j)\) of \(U\). For each \(j\ge1\), choose \(0<\varepsilon_j\le2^{-j}\) so that every mixed derivative of total order at most \(\lfloor j/2\rfloor\) of its summand has supremum at most \(2^{-j}\) on \(K_j\times\mathbb R\). This is possible: for a fixed number \(q<j\) of normal derivatives, the [[real-analysis/scaled-cutoff-estimate|cutoff scaling]] and product rule bound the summand by a constant times \(\varepsilon_j^{j-q}\).

For each fixed compact set and derivative order, all sufficiently late terms obey the geometric bound. The [[analysis/smooth-series-convergence|smooth-series criterion]] proves convergence with every derivative. At \(t=0\), the cutoff is constant near zero, and only the \(j\)-th polynomial contributes to the \(j\)-th normal derivative.

## Support and nonuniqueness

Take \(\varepsilon_0\le1\); then the construction is supported in \(|t|\le1\). If all \(a_j\) are supported in one compact \(K\subset U\), so is the sum in the spatial variable. Two realizations of the same jet differ by a function flat on \(t=0\). A formal Taylor series need not converge even though a smooth realization always exists.

## References

- [Richard Melrose, Lectures on Pseudodifferential Operators, Lecture 2 (Borel summation)](https://math.mit.edu/~rbm/18.157-F05.pdf).

## General increasing-order series

[[asymptotics/shrinking-cutoff-asymptotic-summation|Asymptotic summation by shrinking cutoffs]] allows increasing real decay orders, logarithmic factors, and fixed derivative losses. [[real-analysis/smooth-extension-from-bounded-endpoint-jets|Extension from bounded endpoint jets]] applies this theorem to a function already defined on one side of an endpoint.
