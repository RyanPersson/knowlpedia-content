+++
id = "functional-analysis/banach-algebra-invertible-element"
title = "Invertible element in a Banach algebra"
kind = "definition"
summary = "An element admitting a two-sided multiplicative inverse in a unital Banach algebra."
aliases = ["unit group of a Banach algebra", "Banach-algebra invertibility"]
domains = ["functional-analysis", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["functional-analysis/banach-algebra", "operator-algebras/unitization"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a unital
[[functional-analysis/banach-algebra|Banach algebra]]. An element \(a\in A\)
is **invertible** if there exists \(b\in A\) such that
\[
ab=ba=1_A.
\]
The element \(b\) is unique and is denoted \(a^{-1}\). The invertible elements
form a group \(A^\times\) under multiplication. For a nonunital Banach
algebra, internal invertibility is unavailable; spectral questions are
instead formulated in the
[[operator-algebras/unitization|unitization]] \(\widetilde A\). In
particular, for \(a\in A\), one tests whether
\(\lambda 1_{\widetilde A}-a\) is invertible in \(\widetilde A\), rather than
silently treating \(A\) as unital.

## Openness and the Neumann series

The group \(A^\times\) is open in \(A\), and inversion is continuous. If
\(\|1_A-x\|<1\), then
\[
x^{-1}=\sum_{n=0}^{\infty}(1_A-x)^n.
\]
More generally, if \(a\) is invertible and
\(\|a^{-1}(b-a)\|<1\), the same series shows that \(b\) is invertible. Thus
invertibility is stable under sufficiently small norm perturbations.

## One-sided inverses

In a general Banach algebra, a left inverse need not be a right inverse. For
example, the unilateral shift on a [[linear-algebra/hilbert-space|Hilbert space]] has a left inverse but no
right inverse. The definition therefore requires both equations. In a
commutative algebra the distinction disappears, but existence still depends
on the ambient unital algebra.

## Spectrum and resolvent

The spectrum of \(a\in A\) is
\[
\sigma_A(a)=\{\lambda\in\mathbb C:
\lambda 1_A-a\notin A^\times\},
\]
and its complement is the [[functional-analysis/banach-algebra-resolvent|resolvent set]]. For nonunital \(A\), the same
formula is evaluated in \(\widetilde A\); consequently \(0\) belongs to the
spectrum of every \(a\in A\). This convention makes spectra compatible with
representations and functional calculus.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §1.2 on invertibility, spectra, and resolvents.
2. Theodore W. Palmer, *Banach Algebras and the General Theory of *-Algebras, Volume I*, Cambridge University Press, 1994. [Publisher record](https://doi.org/10.1017/CBO9780511574757). Relevant: Chapter 1 on unital Banach algebras and invertible elements.
