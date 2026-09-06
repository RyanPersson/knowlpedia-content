+++
id = "lie-groups/nelson-analytic-vector-theorem"
title = "Nelson's analytic vector theorem"
kind = "theorem"
summary = "A symmetric operator with a dense set of analytic vectors is essentially self-adjoint."
aliases = ["analytic-vector essential self-adjointness theorem"]
domains = ["lie-groups", "functional-analysis"]
prerequisites = ["functional-analysis/symmetric-operator", "linear-algebra/hilbert-space", "topology/dense-set", "functional-analysis/essentially-self-adjoint-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[functional-analysis/symmetric-operator|symmetric operator]] on a complex [[linear-algebra/hilbert-space|Hilbert space]]. Suppose the domain of \(A\) contains a [[topology/dense-set|dense set]] \(D\) such that every \(v\in D\) is analytic for \(A\):
\[
v\in\bigcap_{n\geq 0}\mathcal D(A^n)
\quad\text{and}\quad
\sum_{n=0}^{\infty}\frac{t_v^n}{n!}\lVert A^n v\rVert<\infty
\]
for some \(t_v>0\). **Nelson's analytic vector theorem** states that \(A\) is [[functional-analysis/essentially-self-adjoint-operator|essentially self-adjoint]]. In particular, its closure is the unique self-adjoint operator extending \(A\) from its stated domain.

## Lie-algebra form

For a representation of a finite-dimensional real [[lie-groups/lie-algebra|Lie algebra]] by skew-symmetric operators \(d\pi(X_j)\) on a common dense invariant domain, form the [[lie-groups/nelson-laplacian|Nelson Laplacian]] \(\Delta=-\sum_j d\pi(X_j)^2\). Essential self-adjointness of \(\Delta\), obtainable from a dense set of [[lie-groups/analytic-vector-unitary-representation|analytic vectors]] for \(\Delta\), supplies analytic vectors for the Lie-algebra action and integrates it to a unitary representation of the [[lie-groups/simply-connected-lie-group|simply connected Lie group]]. It also yields the [[lie-groups/essentially-skew-adjoint-derived-operators|essential skew-adjointness]] of the infinitesimal generators.

## Why analyticity matters

Symmetry alone does not imply essential self-adjointness: symmetric differential operators on incomplete domains may have several [[functional-analysis/self-adjoint-extension|self-adjoint extensions]]. Analyticity supplies convergent power-series control strong enough to prove uniqueness of the unitary evolution. The theorem is therefore a domain criterion, not merely a regularity statement about vectors already known to lie in a unitary representation.

## Conventions and scope

**Warning.** The named theorem appears in two closely related forms: the single symmetric-operator criterion stated in the core and the integrability theorem for Lie-algebra representations. Both require density of analytic vectors on the relevant common domain. Density of smooth vectors alone does not suffice.

## References

1. Edward Nelson, *Analytic vectors*, Annals of Mathematics 70 (1959), 572–615. [DOI record](https://doi.org/10.2307/1970331). Relevant: the analytic-vector criterion and §§8–10 on Lie-algebra exponentiation.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975. [Publisher record](https://www.sciencedirect.com/book/9780125850025/methods-of-modern-mathematical-physics). Relevant: Theorem X.39 and §X.6.
