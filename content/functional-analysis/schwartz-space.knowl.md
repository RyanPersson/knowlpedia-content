+++
id = "functional-analysis/schwartz-space"
title = "Schwartz space on Euclidean space"
kind = "definition"
summary = "The smooth functions whose derivatives decay faster than every inverse polynomial."
aliases = ["Schwartz space", "Schwartz functions", "rapidly decreasing smooth functions", "S(R^n)", "Schwartz topology", "Schwartz seminorms", "Schwartz Fréchet space", "Fréchet topology of the Schwartz space", "space S(R^n)"]
domains = ["functional-analysis", "harmonic-analysis"]
prerequisites = ["real-analysis/partial-derivative", "convex-analysis/seminorm", "functional-analysis/topology-generated-by-seminorms", "functional-analysis/frechet-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **Schwartz space** \(\mathcal S(\mathbb R^n)\) consists of all smooth
functions \(f:\mathbb R^n\to\mathbb C\) such that, for every pair of
multi-indices \(\alpha,\beta\),
\[
p_{\alpha,\beta}(f)
=\sup_{x\in\mathbb R^n}|x^\alpha\partial^\beta f(x)|<\infty.
\]
Here \(\partial^\beta\) denotes an iterated
[[real-analysis/partial-derivative|partial derivative]]. The functions
\(p_{\alpha,\beta}\) are [[convex-analysis/seminorm|seminorms]], and the
[[functional-analysis/topology-generated-by-seminorms|topology they
generate]] is the **Schwartz topology**. With this topology,
\(\mathcal S(\mathbb R^n)\) is a
[[functional-analysis/frechet-space|Fréchet space]]: complete, metrizable,
and locally convex.

## Convergence and rapid decay

A sequence \(f_j\) converges to \(f\) in the Schwartz topology exactly when
\[
p_{\alpha,\beta}(f_j-f)\longrightarrow0
\]
for every \(\alpha,\beta\). Thus convergence controls every derivative,
uniformly after multiplication by every monomial. This is stronger than
[[real-analysis/uniform-convergence|uniform convergence]] of all derivatives and far stronger than pointwise or
\(L^p\) convergence. The seminorm formulation records both smoothness and
rapid decay without choosing a single rate.

## Stability properties

Differentiation, multiplication by a polynomial, translation, and modulation
act continuously on \(\mathcal S(\mathbb R^n)\). The Fourier transform is a
continuous linear bijection of the Schwartz space onto itself with continuous
inverse. These properties make it a natural common domain for Euclidean
Fourier analysis and differential operators.

## Relation to distributions

A [[functional-analysis/tempered-distribution|tempered distribution]] is a
continuous linear functional on the
**topological** [[linear-algebra/vector-space|vector space]] \(\mathcal S(\mathbb R^n)\). It is not a
Schwartz function, and not every algebraic linear functional on the
underlying vector space is tempered. Ordinary distributions are instead
continuous on compactly supported [[functional-analysis/test-function-space|test functions]]; tempered distributions
form the subclass that also acts continuously under the polynomial
growth-and-decay control encoded by the Schwartz topology.

## Fréchet, nuclear, and non-Banach features

The Schwartz space is a nuclear Fréchet space. For \(n\geq1\), its standard
topology cannot be defined by a single norm, so it is not a
[[linear-algebra/banach-space|Banach space]] with that topology. Individual
weighted derivative bounds look norm-like, but the full topology requires
the countable family of all \(p_{\alpha,\beta}\). This distinction is
essential when defining continuity of tempered distributions.

## Examples

Every smooth compactly supported function is a Schwartz function. The
Gaussian \(e^{-|x|^2}\) and every polynomial times a Gaussian also belong to
\(\mathcal S(\mathbb R^n)\). The function
\((1+|x|^2)^{-1}\) is smooth and decays at infinity, but it is not Schwartz:
multiplication by a sufficiently high power of a coordinate makes it
unbounded.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: Chapters 1 and 7.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Publisher record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: the examples of Fréchet and nuclear function spaces.
3. Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley, 1999. [Publisher record](https://www.wiley.com/en-us/Real%2BAnalysis-c-MA34). Relevant: Chapter 8 on distributions and Fourier analysis.
