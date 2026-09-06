+++
id = "functional-analysis/point-continuous-residual-spectrum"
title = "Point, continuous, and residual spectrum"
kind = "definition"
summary = "The standard partition of an operator spectrum according to injectivity and density of the range."
aliases = ["point-continuous-residual decomposition of the spectrum"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/densely-defined-operator", "linear-algebra/banach-space", "functional-analysis/closed-linear-operator", "functional-analysis/spectrum-closed-operator", "linear-algebra/eigenvalue", "shared-foundations/injective-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T:\mathcal D(T)\subseteq X\to X\) be a
[[functional-analysis/densely-defined-operator|densely defined operator]] on a
complex [[linear-algebra/banach-space|Banach space]], and assume that it is
[[functional-analysis/closed-linear-operator|closed]]. A scalar \(\lambda\) in the
[[functional-analysis/spectrum-closed-operator|spectrum]] belongs to the
**point spectrum** when \(T-\lambda I\) is not injective, equivalently when
\(\lambda\) is an [[linear-algebra/eigenvalue|eigenvalue]]. If
\(T-\lambda I\) is injective, then \(\lambda\) belongs to the **continuous
spectrum** when its range is dense but not all of \(X\), and to the
**residual spectrum** when its range is not dense. With this disjoint
convention, these three sets partition the spectrum of a closed operator.

## Hilbert-space description

For a densely defined operator on a complex
[[linear-algebra/hilbert-space|Hilbert space]],
\[
\overline{\operatorname{Ran}(T-\lambda I)}
=\ker(T^*-\overline{\lambda}I)^\perp.
\]
Consequently, an injective \(T-\lambda I\) has non-dense range exactly when
\(\overline{\lambda}\) is an eigenvalue of the
[[functional-analysis/adjoint-unbounded-operator|adjoint]] \(T^*\). A
[[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]]
has no residual spectrum: its spectrum is the disjoint union of its point and
continuous spectra.

## Representative examples

In finite-dimensional spaces every spectral value is an eigenvalue, so the
continuous and residual spectra are empty. Multiplication by the coordinate
function on \(L^2([0,1])\) has spectrum \([0,1]\) and no eigenvalues; every
point of the interval lies in its continuous spectrum. The unilateral shift
\[
S(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots)
\]
on \(\ell^2(\mathbb N)\) is injective, but its range is the closed proper
subspace of sequences whose first coordinate is zero. Thus \(0\) lies in its
residual spectrum.

## Conventions and scope

**Warning.** Some authors define the residual spectrum as all \(\lambda\) for
which \(\operatorname{Ran}(T-\lambda I)\) is not dense, even when
\(T-\lambda I\) is not injective. That convention can overlap the point
spectrum. The definition above instead gives a disjoint partition by testing
noninjectivity first. For operators that are not closed, a bijective
\(T-\lambda I\) can still have an unbounded inverse, so these three tests need
not exhaust every possible spectral failure.

## References

1. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [Publisher record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VII on the point, continuous, and residual spectra.
2. Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II: Spectral Theory*, Interscience, 1963. [Publisher record](https://www.wiley-vch.de/de/fachgebiete/mathematik-und-statistik/linear-operators-part-2-978-0-471-60847-9). Relevant: Chapter VII on spectral subdivisions.
